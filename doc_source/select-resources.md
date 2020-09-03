# Selecting Which Resources AWS Config Records<a name="select-resources"></a>

AWS Config continuously detects when any resource of a supported type is created, changed, or deleted\. AWS Config records these events as configuration items\. You can customize AWS Config to record changes for all supported types of resources or for only those types that are relevant to you\. To learn which types of resources AWS Config can record, see [Supported Resource Types](resource-config-reference.md)\.

## Recording All Supported Resource Types<a name="w22aab9c17c15b5"></a>

By default, AWS Config records the configuration changes for all supported types of *regional resources* that AWS Config discovers in the region in which it is running\. Regional resources are tied to a region and can be used only in that region\. Examples of regional resources are EC2 instances and EBS volumes\.

You can also have AWS Config record supported types of *global resources*\. Global resources are not tied to a specific region and can be used in all regions\. The global resource types that AWS Config supports are IAM users, groups, roles, and customer managed policies\.

**Important**  
The configuration details for a specific global resource are the same in all regions\. If you customize AWS Config in multiple regions to record global resources, AWS Config creates multiple configuration items each time a global resource changes: one configuration item for each region\. These configuration items will contain identical data\. To prevent duplicate configuration items, you should consider customizing AWS Config in only one region to record global resources, unless you want the configuration items to be available in multiple regions\.

## Recording Specific Resource Types<a name="w22aab9c17c15b7"></a>

If you don't want AWS Config to record the changes for all supported resources, you can customize it to record changes for only specific types\. AWS Config records configuration changes for the types of resources that you specify, including the creation and deletion of such resources\.

If a resource is not recorded, AWS Config captures only the creation and deletion of that resource, and no other details, at no cost to you\. When a nonrecorded resource is created or deleted, AWS Config sends a notification, and it displays the event on the resource details page\. The details page for a nonrecorded resource provides null values for most configuration details, and it does not provide information about relationships and configuration changes\.

The relationship information that AWS Config provides for recorded resources is not limited because of missing data for nonrecorded resources\. If a recorded resource is related to a nonrecorded resource, that relationship is provided in the details page of the recorded resource\.

You can stop AWS Config from recording a type of resource any time\. After AWS Config stops recording a resource, it retains the configuration information that was previously captured, and you can continue to access this information\.

AWS Config rules can be used to evaluate compliance for only those resources that AWS Config records\.

## Selecting Resources \(Console\)<a name="select-resources-console"></a>

You can use the AWS Config console to select the types of resources that AWS Config records\.

**To select resources**

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. Open the **Settings** page:
   + If you are using AWS Config in a region that supports AWS Config rules, choose **Settings** in the navigation pane\. For the list of supported regions, see [AWS Config Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#awsconfig_region) in the *Amazon Web Services General Reference*\.
   + Otherwise, choose the settings icon \(![\[settings icon\]](http://docs.aws.amazon.com/config/latest/developerguide/images/gear.png)\) on the **Resource inventory** page\.

1. In the **Resource types to record** section, specify which types of AWS resources you want AWS Config to record:
   + **All resources** – AWS Config records all supported resources with the following options:
     + **Record all resources supported in this region** – AWS Config records configuration changes for every supported type of regional resource\. When AWS Config adds support for a new type of regional resource, it automatically starts recording resources of that type\.
     + **Include global resources** – AWS Config includes supported types of global resources with the resources that it records \(for example, IAM resources\)\. When AWS Config adds support for a new type of global resource, it automatically starts recording resources of that type\.
   + **Specific types** – AWS Config records configuration changes for only those types of AWS resources that you specify\.

1. Save your changes:
   + If you are using AWS Config in a region that supports AWS Config rules, choose **Save**\.
   + Otherwise, choose **Continue**\. In the **AWS Config is requesting permissions to read your resources' configuration** page, choose **Allow**\.

## Selecting Resources \(AWS CLI\)<a name="select-resources-cli"></a>

You can use the AWS CLI to select the types of resources that you want AWS Config to record\. You do this by creating a configuration recorder, which records the types of resources that you specify in a recording group\. In the recording group, you specify whether all supported types or specific types of resources are recorded\.

**To select all supported resources**

1. Use the following [http://docs.aws.amazon.com/cli/latest/reference/configservice/put-configuration-recorder.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/put-configuration-recorder.html) command:

   ```
   $ aws configservice put-configuration-recorder --configuration-recorder name=default,roleARN=arn:aws:iam::123456789012:role/config-role --recording-group allSupported=true,includeGlobalResourceTypes=true
   ```

   This command uses the following options for the `--recording-group` parameter:
   + `allSupported=true` – AWS Config records configuration changes for every supported type of *regional resource*\. When AWS Config adds support for a new type of regional resource, it automatically starts recording resources of that type\.
   + `includeGlobalResourceTypes=true` – AWS Config includes supported types of global resources with the resources that it records\. When AWS Config adds support for a new type of global resource, it automatically starts recording resources of that type\.

     Before you can set this option to `true`, you must set the `allSupported` option to `true`\.

     If you do not want to include global resources, set this option to `false`, or omit it\.

1. \(Optional\) To verify that your configuration recorder has the settings that you want, use the following [http://docs.aws.amazon.com/cli/latest/reference/configservice/describe-configuration-recorders.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/describe-configuration-recorders.html) command:

   ```
   $ aws configservice describe-configuration-recorders
   ```

   The following is an example response:

   ```
   {
       "ConfigurationRecorders": [
           {
               "recordingGroup": {
                   "allSupported": true,
                   "resourceTypes": [],
                   "includeGlobalResourceTypes": true
               },
               "roleARN": "arn:aws:iam::123456789012:role/config-role",
               "name": "default"
           }
       ]
   }
   ```

**To select specific types of resources**

1. Use the `aws configservice` [http://docs.aws.amazon.com/cli/latest/reference/configservice/put-configuration-recorder.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/put-configuration-recorder.html) command, and pass one or more resource types through the `--recording-group` option, as shown in the following example:

   ```
   $ aws configservice put-configuration-recorder --configuration-recorder name=default,roleARN=arn:aws:iam::012345678912:role/myConfigRole --recording-group file://recordingGroup.json
   ```

   The `recordingGroup.json` file specifies which types of resources AWS Config will record:

   ```
   {
     "allSupported": false,
     "includeGlobalResourceTypes": false,
     "resourceTypes": [
       "AWS::EC2::EIP",
       "AWS::EC2::Instance",
       "AWS::EC2::NetworkAcl",
       "AWS::EC2::SecurityGroup",
       "AWS::CloudTrail::Trail",
       "AWS::EC2::Volume",
       "AWS::EC2::VPC",
       "AWS::IAM::User",
       "AWS::IAM::Policy"
     ]
   }
   ```

   Before you can specify resource types for the `resourceTypes` key, you must set the `allSupported` and `includeGlobalResourceTypes` options to false or omit them\.

1. \(Optional\) To verify that your configuration recorder has the settings that you want, use the following [http://docs.aws.amazon.com/cli/latest/reference/configservice/describe-configuration-recorders.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/describe-configuration-recorders.html) command:

   ```
   $ aws configservice describe-configuration-recorders
   ```

   The following is an example response:

   ```
   {
       "ConfigurationRecorders": [
           {
               "recordingGroup": {
                   "allSupported": false,
                   "resourceTypes": [
                       "AWS::EC2::EIP",
                       "AWS::EC2::Instance",
                       "AWS::EC2::NetworkAcl",
                       "AWS::EC2::SecurityGroup",
                       "AWS::CloudTrail::Trail",
                       "AWS::EC2::Volume",
                       "AWS::EC2::VPC",
                       "AWS::IAM::User",
                       "AWS::IAM::Policy"
                   ],
                   "includeGlobalResourceTypes": false
               },
               "roleARN": "arn:aws:iam::123456789012:role/config-role",
               "name": "default"
           }
       ]
   }
   ```