# Query Using the SQL Query Editor AWS CLI<a name="query-using-sql-editor-cli"></a>

To install the AWS Command Line Interface \(AWS CLI\) on your local computer, see [Installing the AWS CLI](http://docs.aws.amazon.com/cli/latest/userguide/installing.html) in the *AWS CLI User Guide*\.

**To query your resource configuration data using the query editor \(AWS CLI\) for a single account and Region**

1. Open a command prompt or a terminal window\.

1. Type the following command to query your resource configuration data\.

   ```
   aws configservice select-resource-config --expression "SELECT resourceId WHERE resourceType='AWS::EC2::Instance'"
   ```

   Depending on your query, the output looks like the following\.

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

**To query your resource configuration data using the query editor \(AWS CLI\) for multiple accounts and Regions**

1. Open a command prompt or a terminal window\.

1. Type the following command to query your resource configuration data\.

   ```
   aws configservice select-aggregate-resource-config --expression "SELECT resourceId WHERE resourceType='AWS::EC2::Instance'" --configuration-aggregator-name my-aggregator
   ```

   Depending on your query, the output looks like the following\.

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
**Note**  
While using the `AWS::IAM::User` resource type in an advanced query, use `awsRegion = 'global'`\. 