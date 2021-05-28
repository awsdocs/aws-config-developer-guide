# Setting Up an Aggregator Using the AWS Command Line Interface<a name="set-up-aggregator-cli"></a>

You can create, view, update, and delete AWS Config aggregator data using the AWS Command Line Interface \(AWS CLI\)\. To use the AWS Management Console, see [Setting Up an Aggregator Using the Console](setup-aggregator-console.md)\.

The AWS CLI is a unified tool to manage your AWS services\. With just one tool to download and configure, you can control multiple AWS services from the command line and use scripts to automate them\.

To install the AWS CLI on your local machine, see [Installing the AWS CLI](http://docs.aws.amazon.com/cli/latest/userguide/installing.html) in the *AWS CLI User Guide*\.

If necessary, type `aws configure` to configure the AWS CLI to use an AWS Region where AWS Config aggregators are available\.

**Topics**
+ [Add an Aggregator Using Individual Accounts](#add-an-aggregator-cli)
+ [Add an Aggregator Using AWS Organizations](#add-an-aggregator-organization-cli)
+ [Register a Delegated Administrator](#register-a-delegated-administrator-cli)
+ [View an Aggregator](#view-an-aggregator-cli)
+ [Edit an Aggregator](#edit-an-aggregator-cli)
+ [Delete an Aggregator](#delete-an-aggregator-cli)
+ [Learn More](#learn-more-setup-console)

## Add an Aggregator Using Individual Accounts<a name="add-an-aggregator-cli"></a>

1. Open a command prompt or a terminal window\.

1. Type the following command to create an aggregator named **MyAggregator**\.

   ```
   aws configservice put-configuration-aggregator --configuration-aggregator-name MyAggregator --account-aggregation-sources "[{\"AccountIds\": [\"AccountID1\",\"AccountID2\",\"AccountID3\"],\"AllAwsRegions\": true}]"
   ```

   For `account-aggregation-sources`, type one of the following\.
   + A comma\-separated list of AWS account IDs for which you want to aggregate data\. Wrap the account IDs in square brackets, and be sure to escape quotation marks \(for example, `"[{\"AccountIds\": [\"AccountID1\",\"AccountID2\",\"AccountID3\"],\"AllAwsRegions\": true}]"`\)\.
   + You can also upload a JSON file of comma\-separated AWS account IDs\. Upload the file using the following syntax: `--account-aggregation-sources MyFilePath/MyFile.json`

     The JSON file must be in the following format:

   ```
   [
       {
           "AccountIds": [
               "AccountID1",
               "AccountID2",
               "AccountID3"
           ],
           "AllAwsRegions": true
       }
   ]
   ```

1. Press Enter to execute the command\.

   You should see output similar to the following:

   ```
   {
       "ConfigurationAggregator": {
           "ConfigurationAggregatorArn": "arn:aws:config:Region:AccountID:config-aggregator/config-aggregator-floqpus3",
           "CreationTime": 1517942461.442,
           "ConfigurationAggregatorName": "MyAggregator",
           "AccountAggregationSources": [
               {
                   "AllAwsRegions": true,
                   "AccountIds": [
                       "AccountID1",
                       "AccountID2",
                       "AccountID3"
                   ]
               }
           ],
           "LastUpdatedTime": 1517942461.442
       }
   }
   ```

## Add an Aggregator Using AWS Organizations<a name="add-an-aggregator-organization-cli"></a>

Before you begin this procedure, you must be signed in to the management account or a registered delegated administrator and all the features must be enabled in your organization\. 

**Note**  
Ensure that the management account registers delegated administrator for AWS Config service principal name \(config\.amazonaws\.com\) before the delegated administrator creates an aggregator\. To register a delegated administrator, see [Register a Delegated Administrator](#register-a-delegated-administrator-cli)\.

1. Open a command prompt or a terminal window\.

1. Type the following command to create an aggregator named **MyAggregator**\.

   ```
   aws configservice put-configuration-aggregator --configuration-aggregator-name MyAggregator --organization-aggregation-source "{\"RoleArn\": \"Complete-Arn\",\"AllAwsRegions\": true}"
   ```

1. Press Enter to execute the command\.

   You should see output similar to the following:

   ```
   {
       "ConfigurationAggregator": {
           "ConfigurationAggregatorArn": "arn:aws:config:Region:AccountID:config-aggregator/config-aggregator-floqpus3",
           "CreationTime": 1517942461.442,
           "ConfigurationAggregatorName": "MyAggregator",
           "OrganizationAggregationSource": {
                   "AllAwsRegions": true,
                   "RoleArn": "arn:aws:config:Region:AccountID:config-aggregator/config-aggregator-floqpus3"
            },
           "LastUpdatedTime": 1517942461.442
       }
   }
   ```

## Register a Delegated Administrator<a name="register-a-delegated-administrator-cli"></a>

Delegated administrators are accounts within a given AWS Organization that are granted additional administrative privileges for a specified AWS service\.

1. Login with management account credentials\.

1. Open a command prompt or a terminal window\.

1. Type the following command to enable service access:

   ```
   aws organizations enable-aws-service-access --service-principal config.amazonaws.com
   ```

1. To verify if the enable service access is complete, type the following command and press Enter to execute the command\.

   ```
   aws organizations list-aws-service-access-for-organization
   ```

   You should see output similar to the following:

   ```
   {
       "EnabledServicePrincipals": [
           {
               "ServicePrincipal": "config.amazonaws.com",
               "DateEnabled": 1607020860.881
           }
       ]
   }
   ```

1. Next, type the following command to register a member account as a delegated administrator for AWS Config\.

   ```
   aws organizations register-delegated-administrator --service-principal config.amazonaws.com --account-id MemberAccountID
   ```

1. To verify if the registration of delegated administrator is complete, type the following command and press Enter to execute the command\.

   ```
   aws organizations list-delegated-administrators --service-principal config.amazonaws.com 
   ```

   You should see output similar to the following:

   ```
   {
       "DelegatedAdministrators": [
           {
               "Id": "MemberAccountID",
               "Arn": "arn:aws:organizations::MemeberAccountID:account/o-c7esubdi38/DelegatedAdministratorAccountID",
               "Email": "name@amazon.com",
               "Name": "name",
               "Status": "ACTIVE",
               "JoinedMethod": "INVITED",
               "JoinedTimestamp": 1604867734.48,
               "DelegationEnabledDate": 1607020986.801
           }
       ]
   }
   ```

## View an Aggregator<a name="view-an-aggregator-cli"></a>

1. Type the following command:

   ```
   aws configservice describe-configuration-aggregators
   ```

1. Depending on your source account you should see output similar to the following:

   **For individuals accounts**

   ```
   {
       "ConfigurationAggregators": [
           {
               "ConfigurationAggregatorArn": "arn:aws:config:Region:AccountID:config-aggregator/config-aggregator-floqpus3",
               "CreationTime": 1517942461.442,
               "ConfigurationAggregatorName": "MyAggregator",
               "AccountAggregationSources": [
                   {
                       "AllAwsRegions": true,
                       "AccountIds": [
                           "AccountID1",
                           "AccountID2",
                           "AccountID3"
                       ]
                   }
               ],
               "LastUpdatedTime": 1517942461.455
           }
       ]
   }
   ```

   OR

   **For an organization**

   ```
   {
       "ConfigurationAggregator": {
           "ConfigurationAggregatorArn": "arn:aws:config:Region:AccountID:config-aggregator/config-aggregator-floqpus3",
           "CreationTime": 1517942461.442,
           "ConfigurationAggregatorName": "MyAggregator",
           "OrganizationAggregationSource": {
                   "AllAwsRegions": true,
                   "RoleArn": "arn:aws:config:Region:AccountID:config-aggregator/config-aggregator-floqpus3"
            },
           "LastUpdatedTime": 1517942461.442
       }
   }
   ```

## Edit an Aggregator<a name="edit-an-aggregator-cli"></a>

1. You can use the `put-configuration-aggregator` command to update or edit a configuration aggregator\.

   Type the following command to add a new account ID to **MyAggregator**:

   ```
   aws configservice put-configuration-aggregator --configuration-aggregator-name MyAggregator --account-aggregation-sources "[{\"AccountIds\": [\"AccountID1\",\"AccountID2\",\"AccountID3\"],\"AllAwsRegions\": true}]"
   ```

1. Depending on your source account you should see output similar to the following:

   **For individuals accounts**

   ```
   {
       "ConfigurationAggregator": {
           "ConfigurationAggregatorArn": "arn:aws:config:Region:AccountID:config-aggregator/config-aggregator-xz2upuu6",
           "CreationTime": 1517952090.769,
           "ConfigurationAggregatorName": "MyAggregator",
           "AccountAggregationSources": [
               {
                   "AllAwsRegions": true,
                   "AccountIds": [
                       "AccountID1",
                       "AccountID2",
                       "AccountID3",
                       "AccountID4"
                   ]
               }
           ],
           "LastUpdatedTime": 1517952566.445
       }
   }
   ```

   OR

   **For an organization**

   ```
   {
       "ConfigurationAggregator": {
           "ConfigurationAggregatorArn": "arn:aws:config:Region:AccountID:config-aggregator/config-aggregator-floqpus3",
           "CreationTime": 1517942461.442,
           "ConfigurationAggregatorName": "MyAggregator",
           "OrganizationAggregationSource": {
                   "AllAwsRegions": true,
                   "RoleArn": "arn:aws:config:Region:AccountID:config-aggregator/config-aggregator-floqpus3"
            },
           "LastUpdatedTime": 1517942461.442
       }
   }
   ```

## Delete an Aggregator<a name="delete-an-aggregator-cli"></a>

**To delete a configuration aggregator using the AWS CLI**
+ Type the following command:

  ```
  aws configservice delete-configuration-aggregator --configuration-aggregator-name MyAggregator
  ```

  If successful, the command executes with no additional output\.

## Learn More<a name="learn-more-setup-console"></a>
+ [Concepts](config-concepts.md)
+ [Authorizing Aggregator Accounts to Collect AWS Config Configuration and Compliance Data Using the AWS Command Line Interface](authorize-aggregator-account-cli.md)
+ [Viewing Compliance Data in the Aggregator Dashboard](viewing-the-aggregate-dashboard.md)
+ [Troubleshooting for Multi\-Account Multi\-Region Data Aggregation](aggregate-data-troubleshooting.md)