# Managing the Configuration Recorder<a name="stop-start-recorder"></a>

AWS Config uses the *configuration recorder* to detect changes in your resource configurations and capture these changes as configuration items\. You must create a configuration recorder before AWS Config can track your resource configurations\.

If you set up AWS Config by using the console or the AWS CLI, AWS Config automatically creates and then starts the configuration recorder for you\. For more information, see [Getting Started with AWS Config](getting-started.md)\.

By default, the configuration recorder records all supported resources in the region where AWS Config is running\. You can create a customized configuration recorder that records only the resource types that you specify\. For more information, see [Selecting Which Resources AWS Config Records](select-resources.md)\.

You are charged service usage fees when AWS Config starts recording configurations\. For pricing information, see [AWS Config Pricing](https://aws.amazon.com/config/pricing/)\. To control costs, you can stop recording by stopping the configuration recorder\. After you stop recording, you can continue to access the configuration information that was already recorded\. You will not be charged AWS Config usage fees until you resume recording\. 

When you start the configuration recorder, AWS Config takes an inventory of all AWS resources in your account\.

## Managing the Configuration Recorder \(Console\)<a name="managing-recorder_console"></a>

You can use the AWS Config console to stop or start the configuration recorder\.

**To stop or start the configuration recorder**

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. Choose **Settings** in the navigation pane\.

1. Stop or start the configuration recorder:
   + If you want to stop recording, under **Recording is on**, choose **Turn off**\. When prompted, choose **Continue**\.
   + If you want to start recording, under **Recording is off**, choose **Turn on**\. When prompted, choose **Continue**\.

## Managing the Configuration Recorder \(AWS CLI\)<a name="managing-recorder_cli"></a>

You can use the AWS CLI to stop or start the configuration recorder\. You can also rename or delete the configuration recorder using the AWS CLI, the AWS Config API, or one of the AWS SDKs\. The following steps help you use the AWS CLI\.

**To stop the configuration recorder**
+ Use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/stop-configuration-recorder.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/stop-configuration-recorder.html) command:

  ```
  $ aws configservice stop-configuration-recorder --configuration-recorder-name configRecorderName
  ```

**To start the configuration recorder**
+ Use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/start-configuration-recorder.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/start-configuration-recorder.html) command:

  ```
  $ aws configservice start-configuration-recorder --configuration-recorder-name configRecorderName
  ```

**To rename the configuration recorder**

To change the configuration recorder name, you must delete it and create a new configuration recorder with the desired name\. 

1. Use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/describe-configuration-recorders.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/describe-configuration-recorders.html) command to look up the name of your current configuration recorder:

   ```
   $ aws configservice describe-configuration-recorders
   {
       "ConfigurationRecorders": [
           {
               "roleARN": "arn:aws:iam::012345678912:role/myConfigRole",
               "name": "default"
           }
       ]
   }
   ```

1. Use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/delete-configuration-recorder.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/delete-configuration-recorder.html) command to delete your current configuration recorder:

   ```
   $ aws configservice delete-configuration-recorder --configuration-recorder-name default
   ```

1. Use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/put-configuration-recorder.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/put-configuration-recorder.html) command to create a configuration recorder with the desired name:

   ```
   $ aws configservice put-configuration-recorder --configuration-recorder name=configRecorderName,roleARN=arn:aws:iam::012345678912:role/myConfigRole
   ```

1. Use the `start-configuration-recorder` command to resume recording:

   ```
   $ aws configservice start-configuration-recorder --configuration-recorder-name configRecorderName
   ```

**To delete the configuration recorder**
+ Use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/delete-configuration-recorder.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/delete-configuration-recorder.html) command:

  ```
  $ aws configservice delete-configuration-recorder --configuration-recorder-name default
  ```