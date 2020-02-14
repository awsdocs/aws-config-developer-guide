# Granting Permissions for AWS Config Administration<a name="grant-permissions-for-config-administration"></a>

To allow users to administer AWS Config, you must grant explicit permissions to IAM users to perform the actions associated with AWS Config tasks\. For most scenarios, you can do this using an AWS managed policy that contains predefined permissions\.

**Note**  
The permissions you grant to users to perform AWS Config administration tasks are not the same as the permissions that AWS Config itself requires in order to deliver log files to Amazon S3 buckets or send notifications to Amazon SNS topics\.

Users who set up and manage AWS Config must have full\-access permissions\. With full\-access permissions, users can provide Amazon S3 and Amazon SNS endpoints that AWS Config delivers data to, create a role for AWS Config, and turn on and turn off recording\.

Users who use AWS Config but don't need to set up AWS Config should have read\-only permissions\. With read\-only permissions, users can look up the configurations of resources or search for resources by tags\.

A typical approach is to create an IAM group that has the appropriate permissions and then add individual IAM users to that group\. For example, you might create an IAM group for users who should have full access to AWS Config actions, and a separate group for users who should be able to view the configurations but not create or change a role\.

**Contents**
+ [Creating an IAM Group and Users for AWS Config Access](#creating-an-IAM-group-user-for-config-access)
+ [Granting Full\-Access Permission for AWS Config Access](#config-full-access-permissions)
+ [Additional Resources](#config-permissions-more-info)

## Creating an IAM Group and Users for AWS Config Access<a name="creating-an-IAM-group-user-for-config-access"></a>

1. Open the IAM console at [https://console\.aws\.amazon\.com/iam](https://console.aws.amazon.com/iam)\.

1. From the dashboard, choose **Groups** in the navigation pane, and then choose **Create New Group**\. 

1. Type a name, and then choose **Next Step**\. 

1. On the **Attach Policy** page, find and choose **AWSConfigUserAccess**\. This policy provides user access to use AWS Config, including searching by tags on resources, and reading all tags\. This does not provide permission to configure AWS Config which requires administrative privileges\.
**Note**  
You can also create a custom policy that grants permissions to individual actions\. For more information, see [Granting Custom Permissions for AWS Config Users ](recommended-iam-permissions-using-aws-config-console-cli.md)\.

1. Choose **Next Step**\.

1. Review the information for the group you are about to create\.
**Note**  
You can edit the group name, but you will need to choose the policy again\.

1. Choose **Create Group**\. The group that you created appears in the list of groups\.

1. Choose the group name that you created, choose **Group Actions**, and then choose **Add Users to Group**\. 

1. On the **Add Users to Group** page, choose the existing IAM users, and then choose **Add Users**\. If you don't already have IAM users, choose **Create New Users**, enter user names, and then choose **Create**\. 

1. If you created new users, choose **Users** in the navigation pane and complete the following for each user: 

   1. Choose the user\.

   1. If the user will use the console to manage AWS Config, in the **Security Credentials** tab, choose **Manage Password**, and then create a password for the user\. 

   1. If the user will use the AWS CLI or API to manage AWS Config, and if you didn't already create access keys, in the **Security Credentials** tab, choose **Manage Access Keys** and then create access keys\. Store the keys in a secure location\.

   1. Give each user his or her credentials \(access keys or password\)\.

## Granting Full\-Access Permission for AWS Config Access<a name="config-full-access-permissions"></a>

1. Sign in to the AWS Identity and Access Management \(IAM\) console at [https://console\.aws\.amazon\.com/iam](https://console.aws.amazon.com/iam)\.

1. In the navigation pane, choose **Policies**, and then choose **Create Policy**\. 

1. For **Create Your Own Policy**, choose **Select**\.

1. Type a policy name and description\. For example: `AWSConfigFullAccess`\.

1. For **Policy Document**, type or paste the full\-access policy into the editor\. You can use the [Full access](recommended-iam-permissions-using-aws-config-console-cli.md#full-config-permission)\.

1. Choose **Validate Policy** and ensure that no errors display in a red box at the top of the screen\. Correct any errors that are reported\. 

1. Choose **Create Policy** to save your new policy\.

1. In the list of policies, select the policy that you created\. You can use the **Filter** menu and the **Search** box to find the policy\.

1. Choose **Policy Actions**, and then choose **Attach**\.

1. Select the users, groups, or roles, and then choose **Attach Policy**\. You can use the **Filter** menu and the **Search** box to filter the list\.

1. Choose **Apply Policy**\. 

**Note**  
Instead of creating a managed policy, you can also create an inline policy from the IAM console and attach it to an IAM user, group, or role\. For more information, see [Working with Inline Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_inline-using.html) in the *IAM User Guide*\.

## Additional Resources<a name="config-permissions-more-info"></a>

To learn more about creating IAM users, groups, policies, and permissions, see [Creating an Admins Group Using the Console](https://docs.aws.amazon.com/IAM/latest/UserGuide/GSGHowToCreateAdminsGroup.html) and [Permissions and Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/PermissionsAndPolicies.html) in the *IAM User Guide*\. 