# Querying the Current Configuration State of AWS Resources<a name="querying-AWS-resources"></a>

AWS Config allows you to query the current configuration state of AWS resources based on configuration properties\. You can perform ad hoc, property\-based queries against current AWS resource state metadata across all resources that AWS Config supports\. The advanced query feature provides a single query endpoint and a powerful query language for obtaining current resource state metadata, without performing service\-specific describe API calls\.

AWS Config uses a subset of structured query language \(SQL\) `SELECT` syntax to perform property\-based queries and aggregations on the current configuration item \(CI\) data\. The queries range in complexity from simple matches against tag and/or resource identifiers, to more complex queries, such as viewing all Amazon S3 buckets that have versioning disabled\. This allows you to query exactly the current resource state you need without performing AWS service\-specific API calls\.

You can use advanced query for: 
+ Inventory management; for example, to retrieve a list of Amazon EC2 instances of a particular size\.
+ Security and operational intelligence; for example, to retrieve a list of resources that have a specific configuration property enabled or disabled\.
+ Cost optimization; for example, to identify a list of Amazon EBS volumes that are not attached to any EC2 instance\.

## Features<a name="query-features"></a>

The query language supports querying AWS resources based on CI properties of all AWS resource types supported by AWS Config, including configuration data, tags, and relationships\. It is a subset of SQL `SELECT` command with limitations, as mentioned in the following section\. It supports aggregation functions such as `AVG`, `COUNT`, `MAX`, `MIN`, and `SUM`\.

## Limitations<a name="query-limitations"></a>

As a subset of SQL `SELECT`, the query syntax has following limitations:
+ No support for `FROM`, `AS`, `JOIN`, `DISTINCT`, `HAVING`, and `ALL` keywords in a query\.
+ When querying against multiple properties within an array of objects, matches are computed against all array elements \(that is, arrays of objects are flattened for indexing\)\. For example, if the database had a document of the form `{ "a": [ { "b": 1, "c": 2, ... }, { "b": 3, "c": 4, ... } ] }`, a query like `SELECT a WHERE a.b=1 AND a.c=4` would match this document, even though no single array element had the specified values of `{ "b": 1, "c": 4 }`\.
+ The `SELECT` all columns shorthand \(that is `SELECT *`\) selects only the top\-level, scalar properties of a CI\. The scalar properties returned are `accountId`, `awsRegion`, `arn`, `availabilityZone`, `configurationItemCaptureTime`, `resourceCreationTime`, `resourceId`, `resourceName`, `resourceType`, and `version`\.
+ Wildcard limitations:
  + Wildcards are supported only for property values and not for property keys \(for example, `...WHERE someKey LIKE 'someValue%'` is supported but `...WHERE 'someKey%' LIKE 'someValue%'` is not supported\)\.
  + Support for only suffix wildcards \(for example, `...LIKE 'AWS::EC2::%'` is supported but `...LIKE '%::EC2::Instance'` is not supported\)\.
  + Wildcard matches must be at least three characters long \(for example, `...LIKE 'ab%'` is not allowed but `...LIKE 'abc%'` is allowed\)\. 
+ Aggregation limitations:
  + `GROUP BY` clauses in aggregations may contain only a single property\.
  + Aggregate functions can accept only a single argument or property\.
  + Aggregate functions cannot take other functions as arguments\.
  + No support for pagination for aggregate queries; a maximum of 500 results is returned\.
  + No support for `HAVING` clauses in aggregations\.

## Query Using the SQL Query Editor \(Console\)<a name="query-using-sql-editor-console"></a>

**Prerequisites**

You must have permissions for the `Config:SelectResource` API\. For more information, see [SelectResourceConfig API](https://docs.aws.amazon.com/config/latest/APIReference/API_SelectResourceConfig.html) in the AWS Config API Reference\.

You must have permissions for the `AWSConfigUserAccess` IAM managed policy\. For more information, see [Granting Permissions for AWS Config Administration](grant-permissions-for-config-administration.md)\.

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. Choose **Advanced query** to query your resource configurations\.

1. On the **Advanced query** page, do one of the following:
   + To use a sample query as a starting point, choose **Sample SQL queries** and then choose an appropriate query from the Sample SQL queries list\. 

     The query is displayed in the SQL query editor\. If required, you can edit this query\.

     OR
   + To create your own query, edit your query in the SQL query editor\.

     An updated list of properties and their data types is available in [GitHub](https://github.com/awslabs/aws-config-resource-schema)\.

1. Choose **Run query**\. The query results are displayed in the table below the query editor\.
**Note**  
The non\-aggregate query results are paginated\. The next page is retrieved automatically by scrolling down\.

## Query Using the SQL Query Editor \(CLI\)<a name="query-using-sql-editor-cli"></a>

To install the AWS CLI on your local machine, see [Installing the AWS CLI](http://docs.aws.amazon.com/cli/latest/userguide/installing.html) in the *AWS CLI User Guide*\.

**To query your resource configuration data using the SQL query editor \(CLI\)**

1. Open a command prompt or a terminal window\.

1. Type the following command to query your resource configuration data\.

   ```
   aws configservice select-resource-config --expression "SELECT resourceId WHERE resourceType='AWS::EC2::Instance'"
   ```

   Depending on your query, the output looks like the following:

   ```
   {
       "QueryInfo": {
           "SelectFields": [
               {
                   "Name": "resourceId"
               }
           ]
       },
       "Results": [
           "{\"resourceId\":\"ResourceId\"}",
           "{\"resourceId\":\"ResourceId\"}",
           "{\"resourceId\":\"ResourceId\"}",
           "{\"resourceId\":\"ResourceId\"}",
           "{\"resourceId\":\"ResourceId\"}",
           "{\"resourceId\":\"ResourceId\"}",
           "{\"resourceId\":\"ResourceId\"}"
       ]
   }
   ```

## Example Queries<a name="example-query"></a>

**Query to list all EC2 instances with AMI ID `ami-12345`** 

```
SELECT
    resourceId,
    resourceType,
    configuration.instanceType,
    configuration.placement.tenancy,
    configuration.imageId,
    availabilityZone
WHERE
    resourceType = 'AWS::EC2::Instance'
    AND configuration.imageId = 'ami-12345'
```

Results

```
{
    "QueryInfo": {
        "SelectFields": [
            {
                "Name": "resourceId"
            },
            {
                "Name": "resourceType"
            },
            {
                "Name": "configuration.instanceType"
            },
            {
                "Name": "configuration.placement.tenancy"
            },
            {
                "Name": "configuration.imageId"
            },
            {
                "Name": "availabilityZone"
            }
        ]
    },
    "Results": [
        "{\"resourceId\":\"resourceid\",\"configuration\":{\"imageId\":\"ami-12345\",\"instanceType\":\"t2.micro\",\"placement\":{\"tenancy\":\"default\"}},\"availabilityZone\":\"us-west-2c\",\"resourceType\":\"AWS::EC2::Instance\"}",
        "{\"resourceId\":\"resourceid\",\"configuration\":{\"imageId\":\"ami-12345\",\"instanceType\":\"t2.micro\",\"placement\":{\"tenancy\":\"default\"}},\"availabilityZone\":\"us-west-2a\",\"resourceType\":\"AWS::EC2::Instance\"}",
        "{\"resourceId\":\"resourceid\",\"configuration\":{\"imageId\":\"ami-12345\",\"instanceType\":\"t2.micro\",\"placement\":{\"tenancy\":\"default\"}},\"availabilityZone\":\"us-west-2c\",\"resourceType\":\"AWS::EC2::Instance\"}",
        "{\"resourceId\":\"resourceid\",\"configuration\":{\"imageId\":\"ami-12345\",\"instanceType\":\"t1.micro\",\"placement\":{\"tenancy\":\"default\"}},\"availabilityZone\":\"us-west-2a\",\"resourceType\":\"AWS::EC2::Instance\"}",
        "{\"resourceId\":\"resourceid\",\"configuration\":{\"imageId\":\"ami-12345\",\"instanceType\":\"t2.micro\",\"placement\":{\"tenancy\":\"default\"}},\"availabilityZone\":\"us-west-2c\",\"resourceType\":\"AWS::EC2::Instance\"}",
        "{\"resourceId\":\"resourceid\",\"configuration\":{\"imageId\":\"ami-12345\",\"instanceType\":\"t2.micro\",\"placement\":{\"tenancy\":\"default\"}},\"availabilityZone\":\"us-west-2c\",\"resourceType\":\"AWS::EC2::Instance\"}",
        "{\"resourceId\":\"resourceid\",\"configuration\":{\"imageId\":\"ami-12345\",\"instanceType\":\"t2.micro\",\"placement\":{\"tenancy\":\"default\"}},\"availabilityZone\":\"us-west-2c\",\"resourceType\":\"AWS::EC2::Instance\"}"
    ]
}
```

**Query for count of resources grouped by their AWS Config rules compliance status** 

```
SELECT
    configuration.complianceType,
    COUNT(*)
WHERE
    resourceType = 'AWS::Config::ResourceCompliance'
GROUP BY
    configuration.complianceType
```

Result

```
{
    "QueryInfo": {
        "SelectFields": [
            {
                "Name": "configuration.complianceType"
            },
            {
                "Name": "COUNT(*)"
            }
        ]
    },
    "Results": [
        "{\"COUNT(*)\":163,\"configuration\":{\"complianceType\":\"NON_COMPLIANT\"}}",
        "{\"COUNT(*)\":2,\"configuration\":{\"complianceType\":\"COMPLIANT\"}}"
    ]
}
```