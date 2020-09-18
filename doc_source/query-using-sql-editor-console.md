# Query Using the SQL Query Editor \(Console\)<a name="query-using-sql-editor-console"></a>

**Prerequisites**

You must have permissions for `config:SelectResourceConfig` and `config:SelectAggregateResourceConfig` APIs\. For more information, see [SelectResourceConfig](https://docs.aws.amazon.com/config/latest/APIReference/API_SelectResourceConfig.html) API and [SelectAggregateResourceConfig](https://docs.aws.amazon.com/config/latest/APIReference/API_SelectAggregateResourceConfig.html) API\.

You must have permissions for the `AWSConfigUserAccess` IAM managed policy\. For more information, see [Granting Permissions for AWS Config Administration](grant-permissions-for-config-administration.md)\.

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. Choose **Advanced queries** from the left navigation to query your resource configurations for a single account and Region or for multiple accounts and Regions\. On the **Advanced queries** page, you can use sample queries or create your own query\.
   + To use a sample query as a starting point, choose an appropriate query from the list of queries\. The query is displayed in the SQL query editor\. If required, you can edit this query\.

     OR
   + To create your own query, choose **New query**\.
**Important**  
An updated list of properties and their data types is available in [GitHub](https://github.com/awslabs/aws-config-resource-schema)\.

1. On the **Query editor** page, for **New query**, create your own query for this account and Region\. You can also select an appropriate aggregator to create a query for multiple accounts and Regions\.
**Note**  
To run a query on an aggregator, create an aggregator\. For more information, see [Setting Up an Aggregator Using the Console](setup-aggregator-console.md)\. If you already have an aggregator set up, in the query scope, choose the aggregator to run an advanced query on that aggregator\. When you select an aggregator, consider adding the AWS account ID and AWS Region in the query statement to view that information in the results\.

1. Choose **Run**\. The query results are displayed in the table below the query editor\.

1. Choose **Export as** to export the query results in CSV or JSON format\.
**Note**  
The query results are paginated\. When you choose export, up to 500 results are exported\.   
You can also use the APIs to retrieve all the results\. The results are paginated and you can retrieve 100 results at a time\.