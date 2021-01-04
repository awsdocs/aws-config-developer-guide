# Query Using the SQL Query Editor \(Console\)<a name="query-using-sql-editor-console"></a>

You can either use AWS sample queries or you can create your own query called as custom queries\.

**Prerequisites**

You must have permissions for `config:SelectResourceConfig` and `config:SelectAggregateResourceConfig` APIs\. For more information, see [SelectResourceConfig](https://docs.aws.amazon.com/config/latest/APIReference/API_SelectResourceConfig.html) API and [SelectAggregateResourceConfig](https://docs.aws.amazon.com/config/latest/APIReference/API_SelectAggregateResourceConfig.html) API\.

You must have permissions for the `AWSConfigUserAccess` IAM managed policy\. For more information, see [Granting Permissions for AWS Config Administration](grant-permissions-for-config-administration.md)\.

If you are using `AWSServiceRoleForConfig` \(service linked role\) or `AWSConfigRole`, you will have permissions to save a query\. If you are not using either of these roles, you must have permissions to `config:PutStoredQuery`, `config:GetStoredQuery`, `config:TagResource`, `config:UntagResource`, `config:ListTagsForResource` and `config:GetResources`\. 

## Use an AWS Sample Query<a name="use-a-sample-query"></a>

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. Choose **Advanced queries** from the left navigation to query your resource configurations for a single account and Region or for multiple accounts and Regions\.

1. On the **Advanced queries** page, choose an appropriate query from the list of queries\. You can filter a query either by the name, description, creator or tags\. To filter AWS queries, choose **Creater** and enter **AWS**\. The query is displayed in the SQL query editor\. If required, you can edit this query\.
**Important**  
An updated list of properties and their data types is available in [GitHub](https://github.com/awslabs/aws-config-resource-schema)\.
**Note**  
To run a query on an aggregator, create an aggregator\. For more information, see [Setting Up an Aggregator Using the Console](setup-aggregator-console.md)\. If you already have an aggregator set up, in the query scope, choose the aggregator to run an advanced query on that aggregator\. When you select an aggregator, consider adding the AWS account ID and AWS Region in the query statement to view that information in the results\.

1. To save this query to a new query, choose **Save As**\.
   + In the **Query Name** field, update the name of the query\.
   + In the **Description** field, update the description of the query\.
   + Enter up to 50 unique tags for this query\.
   + Choose **Save**\.

1. Choose **Run**\. The query results are displayed in the table below the query editor\.

1. Choose **Export as** to export the query results in CSV or JSON format\.
**Note**  
The query results are paginated\. When you choose export, upto 500 results are exported\.  
You can also use the APIs to retrieve all the results\. The results are paginated and you can retrieve 100 results at a time\.

## Create your custom query<a name="create-you-custom-use-query"></a>

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. Choose **Advanced queries** from the left navigation to query your resource configurations for a single account and Region or for multiple accounts and Regions\.

1. To create your custom query, choose **New query**\.
**Important**  
An updated list of properties and their data types is available in [GitHub](https://github.com/awslabs/aws-config-resource-schema)\.
**Note**  
To view or edit a custom query, filter a query either by the name, description, creator or tags\. To filter custom queries, choose **Creater** and enter **Custom**\.

1. On the **Query editor** page, create your own query for this account and Region\. You can also select an appropriate aggregator to create a query for multiple accounts and Regions\.
**Note**  
To run a query on an aggregator, create an aggregator\. For more information, see [Setting Up an Aggregator Using the Console](setup-aggregator-console.md)\. If you already have an aggregator set up, in the query scope, choose the aggregator to run an advanced query on that aggregator\. When you select an aggregator, consider adding the AWS account ID and AWS Region in the query statement to view that information in the results\.

1. Edit if you wish you make changes to this query\. Choose **Save Query** to save this query\.
   + In the **Query Name** field, update the name of the query\.
   + In the **Description** field, update the description of the query\.
   + Enter up to 50 unique tags for this query\.
   + Choose **Save**\.

1. Choose **Run**\. The query results are displayed in the table below the query editor\.

1. Choose **Export as** to export the query results in CSV or JSON format\.
**Note**  
The query results are paginated\. When you choose export, upto 500 results are exported\.  
You can also use the APIs to retrieve all the results\. The results are paginated and you can retrieve 100 results at a time\.