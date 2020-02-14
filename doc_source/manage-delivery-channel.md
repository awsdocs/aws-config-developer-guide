# Managing the Delivery Channel<a name="manage-delivery-channel"></a>

As AWS Config continually records the changes that occur to your AWS resources, it sends notifications and updated configuration states through the *delivery channel*\. You can manage the delivery channel to control where AWS Config sends configuration updates\.

You can have only one delivery channel per region per AWS account, and the delivery channel is required to use AWS Config\.

## Updating the Delivery Channel<a name="update-dc-console"></a>

When you update the delivery channel, you can set the following options:
+ The Amazon S3 bucket to which AWS Config sends configuration snapshots and configuration history files\.
+ How often AWS Config delivers configuration snapshots to your Amazon S3 bucket\.
+ The Amazon SNS topic to which AWS Config sends notifications about configuration changes\.

**To update the delivery channel \(console\)**
+ You can use the AWS Config console to set the Amazon S3 bucket and the Amazon SNS topic for your delivery channel\. For steps to manage these settings, see [Setting Up AWS Config with the Console](gs-console.md)\.

  The console does not provide options to rename the delivery channel, set the frequency for configuration snapshots, or delete the delivery channel\. To do these tasks, you must use the AWS CLI, the AWS Config API, or one of the AWS SDKs\.

**To update the delivery channel \(AWS CLI\)**

1. Use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/put-delivery-channel.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/put-delivery-channel.html) command:

   ```
   $ aws configservice put-delivery-channel --delivery-channel file://deliveryChannel.json
   ```

   The deliveryChannel\.json file specifies the delivery channel attributes:

   ```
   {
       "name": "default",
       "s3BucketName": "config-bucket-123456789012",
       "snsTopicARN": "arn:aws:sns:us-east-2:123456789012:config-topic",
       "configSnapshotDeliveryProperties": {
           "deliveryFrequency": "Twelve_Hours"
       }
   }
   ```

   This example sets the following attributes:
   + `name` – The name of the delivery channel\. By default, AWS Config assigns the name `default` to a new delivery channel\.

     You cannot update the delivery channel name with the `put-delivery-channel` command\. For the steps to change the name, see [Renaming the Delivery Channel](#update-dc-rename)\.
   + `s3BucketName` – The name of the Amazon S3 bucket to which AWS Config delivers configuration snapshots and configuration history files\.

     If you specify a bucket that belongs to another AWS account, that bucket must have policies that grant access permissions to AWS Config\. For more information, see [Permissions for the Amazon S3 Bucket](s3-bucket-policy.md)\.
   + `snsTopicARN` – The Amazon Resource Name \(ARN\) of the Amazon SNS topic to which AWS Config sends notifications about configuration changes\.

     If you choose a topic from another account, that topic must have policies that grant access permissions to AWS Config\. For more information, see [Permissions for the Amazon SNS Topic](sns-topic-policy.md)\.
   + `configSnapshotDeliveryProperties` – Contains the `deliveryFrequency` attribute, which sets how often AWS Config delivers configuration snapshots\.

1. \(Optional\) You can use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/describe-delivery-channels.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/describe-delivery-channels.html) command to verify that the delivery channel settings are updated:

   ```
   $ aws configservice describe-delivery-channels
   {
       "DeliveryChannels": [
           {
               "configSnapshotDeliveryProperties": {
                   "deliveryFrequency": "Twelve_Hours"
               },
               "snsTopicARN": "arn:aws:sns:us-east-2:123456789012:config-topic",
               "name": "default",
               "s3BucketName": "config-bucket-123456789012"
           }
       ]
   }
   ```

## Renaming the Delivery Channel<a name="update-dc-rename"></a>

To change the delivery channel name, you must delete it and create a new delivery channel with the desired name\. Before you can delete the delivery channel, you must temporarily stop the configuration recorder\.

The AWS Config console does not provide the option to delete the delivery channel, so you must use the AWS CLI, the AWS Config API, or one of the AWS SDKs\. 

**To rename the delivery channel \(AWS CLI\)**

1. Use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/stop-configuration-recorder.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/stop-configuration-recorder.html) command to stop the configuration recorder:

   ```
   $ aws configservice stop-configuration-recorder --configuration-recorder-name configRecorderName
   ```

1. Use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/describe-delivery-channels.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/describe-delivery-channels.html) command, and take note of your delivery channel's attributes:

   ```
   $ aws configservice describe-delivery-channels
   {
       "DeliveryChannels": [
           {
               "configSnapshotDeliveryProperties": {
                   "deliveryFrequency": "Twelve_Hours"
               },
               "snsTopicARN": "arn:aws:sns:us-east-2:123456789012:config-topic",
               "name": "default",
               "s3BucketName": "config-bucket-123456789012"
           }
       ]
   }
   ```

1. Use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/delete-delivery-channel.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/delete-delivery-channel.html) command to delete the delivery channel:

   ```
   $ aws configservice delete-delivery-channel --delivery-channel-name default
   ```

1. Use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/put-delivery-channel.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/put-delivery-channel.html) command to create a delivery channel with the desired name:

   ```
   $ aws configservice put-delivery-channel --delivery-channel file://deliveryChannel.json
   ```

   The deliveryChannel\.json file specifies the delivery channel attributes:

   ```
   {
       "name": "myCustomDeliveryChannelName",
       "s3BucketName": "config-bucket-123456789012",
       "snsTopicARN": "arn:aws:sns:us-east-2:123456789012:config-topic",
       "configSnapshotDeliveryProperties": {
           "deliveryFrequency": "Twelve_Hours"
       }
   }
   ```

1. Use the `start-configuration-recorder` command to resume recording:

   ```
   $ aws configservice start-configuration-recorder --configuration-recorder-name configRecorderName
   ```