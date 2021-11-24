# Querying the Current Configuration State of AWS Resources<a name="querying-AWS-resources"></a>

You can use AWS Config to query the current configuration state of AWS resources based on configuration properties for a single account and Region or across multiple accounts and Regions\. You can perform ad hoc, property\-based queries against current AWS resource state metadata across all resources that AWS Config supports\. The **advanced query** feature provides a single query endpoint and a powerful query language to get current resource state metadata without performing service\-specific describe API calls\. You can use configuration aggregators to run the same queries from a central account across multiple accounts and AWS Regions\. 

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

## Limitations<a name="query-limitations"></a>

As a subset of SQL `SELECT`, the query syntax has following limitations:
+ No support for `ALL`, `AS`, `DISTINCT`, `FROM`, `HAVING`, `JOIN`, and `UNION` keywords in a query\. `NULL` value queries are not supported\.
+ No support for querying on third\-party resources\. Third\-party resources retrieved using advanced queries will have the configuration field set as `NULL`\.
+ No support for nested structures \(such as tags\) to be unpacked with SQL queries\.
+ When querying against multiple properties within an array of objects, matches are computed against all the array elements\. For example, for a resource R with rules A and B, the resource is compliant to rule A but noncompliant to rule B\. The resource R is stored as: 

  ```
  { 
  configRuleList: [ 
  { configRuleName: 'A', complianceType: 'compliant' }, 
  { configRuleName: 'B', complianceType: 'non_compliant' } 
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

## Region Support<a name="query-regionsupport"></a>

Advanced queries is supported in the following Regions:


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/querying-AWS-resources.html)

\*Saved queries is not available in Africa \(Cape Town\) and Europe \(Milan\) Regions\. 

\*Advanced queries for multi\-account multi\-regions is not available in Africa \(Cape Town\), Europe \(Milan\), China \(Beijing\), and China \(Ningxia\) Regions\.