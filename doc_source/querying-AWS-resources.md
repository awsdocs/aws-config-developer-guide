# Querying the Current Configuration State of AWS Resources<a name="querying-AWS-resources"></a>

You can use AWS Config to query the current configuration state of AWS resources based on configuration properties for a single account and Region or across multiple accounts and Regions\. You can perform ad hoc, property\-based queries against current AWS resource state metadata across a list of resources that AWS Config supports\. For more information on the list of supported resource types, see [Supported Resource Types for Advanced Queries](https://github.com/awslabs/aws-config-resource-schema/tree/master/config/properties/resource-types)\.

The **advanced query** feature provides a single query endpoint and a powerful query language to get current resource state metadata without performing service\-specific describe API calls\. You can use configuration aggregators to run the same queries from a central account across multiple accounts and AWS Regions\. 

AWS Config uses a subset of structured query language \(SQL\) `SELECT` syntax to perform property\-based queries and aggregations on the current configuration item \(CI\) data\. The queries range in complexity from simple matches against tag and/or resource identifiers, to more complex queries, such as viewing all Amazon S3 buckets that have versioning disabled\. This allows you to query exactly the current resource state you need without performing AWS service\-specific API calls\.

You can use advanced query for: 
+ Inventory management; for example, to retrieve a list of Amazon EC2 instances of a particular size\.
+ Security and operational intelligence; for example, to retrieve a list of resources that have a specific configuration property enabled or disabled\.
+ Cost optimization; for example, to identify a list of Amazon EBS volumes that are not attached to any EC2 instance\.
+ Compliance data; for example, to retrieve a list of all your conformance packs and their compliance status\.

**Topics**
+ [Features](#query-features)
+ [Limitations](#query-limitations)
+ [Region Support](#query-regionsupport)
+ [Query Using the SQL Query Editor \(Console\)](query-using-sql-editor-console.md)
+ [Query Using the SQL Query Editor \(AWS CLI\)](query-using-sql-editor-cli.md)
+ [Example Queries](example-query.md)
+ [Example Relationship Queries](examplerelationshipqueries.md)
+ [Query Components](query-components.md)

## Features<a name="query-features"></a>

The query language supports querying AWS resources based on CI properties of all AWS resource types supported by AWS Config, including configuration data, tags, and relationships\. It is a subset of SQL `SELECT` command with limitations, as mentioned in the following section\. It supports aggregation functions such as `AVG`, `COUNT`, `MAX`, `MIN`, and `SUM`\.

**Note**  
Advanced queries supports a subset of the resource types supported by AWS Config\. For a list of those supported resource types, see [Supported Resource Types for Advanced Queries](https://github.com/awslabs/aws-config-resource-schema/tree/master/config/properties/resource-types)\.

## Limitations<a name="query-limitations"></a>

**Note**  
Advance query does not support querying resources which have not been configured to be recorded by the configuration recorder\. AWS Config creates Configuration Items \(CIs\) with `ResourceNotRecorded` in the `configurationItemStatus` when a resource has been discovered but is not configured to be recorded by the configuration recorder\. While an aggregator will aggregate these CIs, advanced query does not support querying CIs with `ResourceNotRecorded`\. Update your recorder settings to enable recording of the resource types that you want to query\.

As a subset of SQL `SELECT`, the query syntax has following limitations:
+ No support for `ALL`, `AS`, `DISTINCT`, `FROM`, `HAVING`, `JOIN`, and `UNION` keywords in a query\. `NULL` value queries are not supported\.
+ No support for querying on third\-party resources\. Third\-party resources retrieved using advanced queries will have the configuration field set as `NULL`\.
+ No support for nested structures \(such as tags\) to be unpacked with SQL queries\.
+ CIDR notation is converted to IP ranges for search\. This means that `"="` and `"BETWEEN"` search for any range that includes the provided IP, instead of for an exact one\. To search for an exact IP range, you need to add in additional conditions to exclude IPs outside of the range\. For example, to search for 10\.0\.0\.0/24 and only that IP block, you can do:

  ```
  SELECT * WHERE resourceType = 'AWS::EC2::SecurityGroup'
    AND configuration.ipPermissions.ipRanges BETWEEN '10.0.0.0'
    AND '10.0.0.255'
    AND NOT configuration.ipPermissions.ipRanges < '10.0.0.0'
    AND NOT configuration.ipPermissions.ipRanges > '10.0.0.255'
  ```

  For 192\.168\.0\.2/32, you can search in a similar fashion:

  ```
  SELECT * WHERE resourceType = 'AWS::EC2::SecurityGroup'
    AND configuration.ipPermissions.ipRanges = '192.168.0.2'
    AND NOT configuration.ipPermissions.ipRanges > '192.168.0.2'
    AND NOT configuration.ipPermissions.ipRanges < '192.168.0.2'
  ```
+ When querying against multiple properties within an array of objects, matches are computed against all the array elements\. For example, for a resource R with rules A and B, the resource is compliant to rule A but noncompliant to rule B\. The resource R is stored as: 

  ```
  { 
      configRuleList: [ 
          {
              configRuleName: 'A', complianceType: 'compliant'
          }, 
          {   
              configRuleName: 'B', complianceType: 'non_compliant'
          } 
      ]
  }
  ```

  R will be returned by this query:

  ```
  SELECT configuration WHERE configuration.configRuleList.complianceType = 'non_compliant' 
  AND configuration.configRuleList.configRuleName = 'A'
  ```

  The first condition `configuration.configRuleList.complianceType = 'non_compliant'` is applied to ALL elements in R\.configRuleList, because R has a rule \(rule B\) with complianceType = ‘non\_compliant’, the condition is evaluated as true\. The second condition `configuration.configRuleList.configRuleName` is applied to ALL elements in R\.configRuleList, because R has a rule \(rule A\) with configRuleName = ‘A’, the condition is evaluated as true\. As both conditions are true, R will be returned\.
+ The `SELECT` all columns shorthand \(that is `SELECT *`\) selects only the top\-level, scalar properties of a CI\. The scalar properties returned are `accountId`, `awsRegion`, `arn`, `availabilityZone`, `configurationItemCaptureTime`, `resourceCreationTime`, `resourceId`, `resourceName`, `resourceType`, and `version`\.
+ Wildcard limitations:
  + Wildcards are supported only for property values and not for property keys \(for example, `...WHERE someKey LIKE 'someValue%'` is supported but `...WHERE 'someKey%' LIKE 'someValue%'` is not supported\)\.
  + Support for only suffix wildcards \(for example, `...LIKE 'AWS::EC2::%'` and `...LIKE 'AWS::EC2::_'` is supported but `...LIKE '%::EC2::Instance'` and `...LIKE '_::EC2::Instance'`is not supported\)\.
  + Wildcard matches must be at least three characters long \(for example, `...LIKE 'ab%'` and `...LIKE 'ab_'` is not allowed but `...LIKE 'abc%'` and `...LIKE 'abc_'` is allowed\)\. 
**Note**  
The "`_`" \(single underscore\) is also treated as a wildcard\.
+ Aggregation limitations:
  + Aggregate functions can accept only a single argument or property\.
  + Aggregate functions cannot take other functions as arguments\.
  + `GROUP BY` with an `ORDER BY` clause referencing aggregate functions may contain only a single property\.
  + For all other aggregations `GROUP BY` clauses may contain up to three properties\.
  + Pagination is supported for all aggregate queries except when `ORDER BY` clause has an aggregate function\. For example, `GROUP BY X, ORDER BY Y` does not work if `Y` is an aggregate function\.
  + No support for `HAVING` clauses in aggregations\.
+ Mismatched identifier limitations:

  Mismatched identifiers are properties that have the same spelling but different cases \(upper and lower case\)\. Advanced query does not support processing queries that contain mismatched identifiers\. For example:
  + Two properties that have the exact same spelling but with different casing \(`configuration.dbclusterIdentifier` and `configuration.dBClusterIdentifier`\)\.
  + Two properties where one property is a subset of the other, and they have different casing \(`configuration.ipAddress` and `configuration.ipaddressPermissions`\)\.

## Region Support<a name="query-regionsupport"></a>

Advanced queries is supported in the following Regions:


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/querying-AWS-resources.html)

\*Saved queries is not available in China \(Beijing\), and China \(Ningxia\) Regions\.

\*Advanced queries for multi\-account multi\-regions is not available in China \(Beijing\), and China \(Ningxia\) Regions\.