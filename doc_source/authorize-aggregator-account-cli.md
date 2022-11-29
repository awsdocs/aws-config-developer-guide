# Authorizing Aggregator Accounts to Collect AWS Config Configuration and Compliance Data Using the AWS Command Line Interface<a name="authorize-aggregator-account-cli"></a>

You can authorize aggregator accounts to collect AWS Config data from source accounts and delete aggregator accounts using the AWS Command Line Interface \(AWS CLI\)\. To use the AWS Management Console, see [Authorizing Aggregator Accounts to Collect AWS Config Configuration and Compliance Data Using the Console](authorize-aggregator-account-console.md)\.

The AWS CLI is a unified tool to manage your AWS services\. With just one tool to download and configure, you can control multiple AWS services from the command line and use scripts to automate them\. For more information about the AWS CLI and for instructions on installing the AWS CLI tools, see the following in the *AWS Command Line Interface User Guide*\.
+ [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/)
+ [Getting Set Up with the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html) 

If necessary, type `aws configure` to configure the AWS CLI to use an AWS Region where AWS Config conformance packs are available\.

**Topics**
+ [Add Authorization for Aggregator Accounts and Regions](#add-authorization-cli)
+ [Delete an Authorization Account](#delete-authorization-cli)
+ [Learn More](#learn-more-setup-console)

## Add Authorization for Aggregator Accounts and Regions<a name="add-authorization-cli"></a>

1. Open a command prompt or a terminal window\.

1. Type the following command:

   ```
   aws configservice put-aggregation-authorization --authorized-account-id  AccountID --authorized-aws-region Region
   ```

1. Press Enter\.

   You should see output similar to the following:

   ```
   {
       "AggregationAuthorization": {
           "AuthorizedAccountId": "AccountID",
           "AggregationAuthorizationArn": "arn:aws:config:Region:AccountID:aggregation-authorization/AccountID/Region",
           "CreationTime": 1518116709.993,
           "AuthorizedAwsRegion": "Region"
       }
   }
   ```

## Delete an Authorization Account<a name="delete-authorization-cli"></a>

**To delete an authorized account using the AWS CLI**
+ Type the following command:

  ```
  aws configservice delete-aggregation-authorization --authorized-account-id  AccountID --authorized-aws-region Region
  ```

  If successful, the command executes with no additional output\.

## Learn More<a name="learn-more-setup-console"></a>
+ [Concepts](config-concepts.md)
+ [Setting Up an Aggregator Using the AWS Command Line Interface](set-up-aggregator-cli.md)
+ [Viewing Compliance Data in the Aggregator Dashboard](viewing-the-aggregate-dashboard.md)
+ [Troubleshooting for Multi\-Account Multi\-Region Data Aggregation](aggregate-data-troubleshooting.md)