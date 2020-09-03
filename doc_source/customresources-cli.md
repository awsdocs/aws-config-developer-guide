# Record and Delete a Configuration State for Third\-Party Resources Using AWS CLI<a name="customresources-cli"></a>

The AWS CLI is a unified tool to manage your AWS services\. With just one tool to download and configure, you can control multiple AWS services from the command line and use scripts to automate them\.

To install the AWS CLI on your local machine, see [Installing the AWS CLI](http://docs.aws.amazon.com/cli/latest/userguide/installing.html) in the *AWS CLI User Guide*\.

If necessary, type `aws configure` to configure the AWS CLI\.

**Topics**
+ [Record a Configuration Item](#add-custom-resource-type-cli)
+ [Read the Configuration Item using AWS Config APIs](#view-custom-resource-type-cli)
+ [Delete the Third\-Party Resource](#delete-custom-resource-type)

## Record a Configuration Item<a name="add-custom-resource-type-cli"></a>

Record a configuration item for a third\-party resource or a custom resource type using the following procedure:

Ensure you register the resource type `MyCustomNamespace::Testing::WordPress` with its matching schema\.

1. Open a command prompt or a terminal window\.

1. Type the following command:

   ```
   aws configservice put-resource-config --resource-type MyCustomNamespace::Testing::WordPress --resource-id resource-001 --schema-version-id 00000001 --configuration  '{
     "Id": "resource-001",
     "Name": "My example custom resource.",
     "PublicAccess": false
   }'
   ```

## Read the Configuration Item using AWS Config APIs<a name="view-custom-resource-type-cli"></a>

1. Open a command prompt or a terminal window\.

1. Type the following command:

   ```
   aws configservice list-discovered-resources --resource-type MyCustomNamespace::Testing::WordPress
   ```

1. Press Enter\.

   You should see output similar to the following:

   ```
   {
       "resourceIdentifiers": [
           {
               "resourceType": "MyCustomNamespace::Testing::WordPress",
               "resourceId": "resource-001"
           }
       ]
   }
   ```

1. Type the following command:

   ```
   aws configservice batch-get-resource-config --resource-keys '[ { "resourceType": "MyCustomNamespace::Testing::WordPress", "resourceId": "resource-001" } ]'
   ```

1. Press Enter\.

   You should see output similar to the following:

   ```
   {
       "unprocessedResourceKeys": [],
       "baseConfigurationItems": [
           {
               "configurationItemCaptureTime": 1569605832.673,
               "resourceType": "MyCustomNamespace::Testing::WordPress",
               "resourceId": "resource-001",
               "configurationStateId": "1569605832673",
               "awsRegion": "us-west-2",
               "version": "1.3",
               "supplementaryConfiguration": {},
               "configuration": "{\"Id\":\"resource-001\",\"Name\":\"My example custom resource.\",\"PublicAccess\":false}",
               "configurationItemStatus": "ResourceDiscovered",
               "accountId": "AccountId"
           }
       ]
   }
   ```

## Delete the Third\-Party Resource<a name="delete-custom-resource-type"></a>

You can record the configuration state for a third\-party resouce or custom resource type that you want to delete\.
+ Type the following command:

  ```
  aws configservice delete-resource-config --resource-type MyCustomNamespace::Testing::WordPress --resource-id resource-002
  ```

  If successful, the command executes with no additional output\.