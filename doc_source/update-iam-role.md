# Updating the IAM Role Assigned to AWS Config<a name="update-iam-role"></a>

You can update the IAM role assumed by AWS Config any time\. Before you update the IAM role, ensure that you have created a new role to replace the old one\. You must attach policies to the new role that grant permissions to AWS Config to record configurations and deliver them to your delivery channel\. In addition, make sure to copy the Amazon Resource Name \(ARN\) of your new IAM role\. You will need it to update the IAM role\. For information about creating an IAM role and attaching the required policies to the IAM role, see [Creating an IAM Role](gs-cli-prereq.md#gs-cli-create-iamrole)\.

**Note**  
To find the ARN of an existing IAM role, go to the IAM console at [https://console\.aws\.amazon\.com/iam/](https://console.aws.amazon.com/iam/)\. Choose **Roles** in the navigation pane\. Then choose the name of the desired role and find the ARN at the top of the **Summary** page\.

## Updating the IAM Role<a name="update-iam-role-console"></a>

You can update your IAM role using the AWS Management Console or the AWS CLI\.

**To update the IAM role in a region where rules are supported \(console\)**

If you are using AWS Config in a region that supports AWS Config rules, complete the following steps\. For the list of supported regions, see [AWS Config Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#awsconfig_region) in the *Amazon Web Services General Reference*\.

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. Choose **Settings** in the navigation pane\.

1. In the **AWS Config role**, section, choose the IAM role:
   + **Create a role** – AWS Config creates a role that has the required permissions\. For **Role name**, you can customize the name that AWS Config creates\.
   + **Choose a role from your account** – For **Role name**, choose an IAM role in your account\. AWS Config will attach the required policies\. For more information, see [Permissions for the IAM Role Assigned to AWS Config](iamrole-permissions.md)\.
**Note**  
Check the box if you want to use the IAM role as it\. AWS Config will not attach policies to the role\.

1. Choose **Save**\.

**To update the IAM role in a region where rules are not supported \(console\)**

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. On the **Resource inventory** page, choose the settings icon \(![\[settings icon\]](http://docs.aws.amazon.com/config/latest/developerguide/images/gear.png)\)\.

1. Choose **Continue**\.

1. In the **AWS Config is requesting permissions to read your resources' configuration** page, choose **View Details**\.

1. In the **Role Summary** section, choose the IAM role:
   + If you want to create a role, for **IAM Role**, choose **Create a new IAM Role**\. Then type a name for **Role Name**\.
   + If you want to use an existing role, select it for **IAM Role**\. Then, for **Policy Name**, select an available policy or create one by selecting **Create a new Role Policy**\.

1. Choose **Allow**\.<a name="update-iam-role-cli"></a>

**To update the IAM role \(AWS CLI\)**
+ Use the [http://docs.aws.amazon.com/cli/latest/reference/configservice/put-configuration-recorder.html](http://docs.aws.amazon.com/cli/latest/reference/configservice/put-configuration-recorder.html) command and specify the Amazon Resource Name \(ARN\) of the new role:

  ```
  $ aws configservice put-configuration-recorder --configuration-recorder name=configRecorderName,roleARN=arn:aws:iam::012345678912:role/myConfigRole
  ```