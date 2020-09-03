# Remediating Noncompliant AWS Resources by AWS Config Rules<a name="remediation"></a>

 AWS Config allows you to remediate noncompliant resources that are evaluated by AWS Config Rules\. AWS Config applies remediation using [AWS Systems Manager Automation documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)\. These documents define the actions to be performed on noncompliant AWS resources evaluated by AWS Config Rules\. You can associate SSM documents by using AWS Management Console or by using APIs\.

AWS Config provides a set of managed automation documents with remediation actions\. You can also create and associate custom automation documents with AWS Config rules\. 

To apply remediation on noncompliant resources, you can either choose the remediation action you want to associate from a prepopulated list or create your own custom remediation actions using SSM documents\. AWS Config provides a recommended list of remediation action in the AWS Management Console\. 

In the AWS Management Console, you can either choose to **manually** or **automatically** remediate noncompliant resources by associating remediation actions with AWS Config rules\. With all remediation actions, you can either choose manual or automatic remediation\.

**Topics**
+ [Prerequisite](#prerequisite)
+ [Setting Up Manual Remediation \(Console\)](#setup-manualremediation)
+ [Setting Up Auto Remediation \(Console\)](#setup-autoremediation)
+ [Setting Up and Applying a Remediation Action Remediation Using Rules and Resources \(Console\)](#remediation-using-rules-resources-page)
+ [Delete Remediation Action \(Console\)](#delete-remediation-action)
+ [Managing Remediation \(API\)](#remediate-api)

## Prerequisite<a name="prerequisite"></a>

Before you begin to apply remediation on noncompliant resources, you must select a rule and set up remediation \(manual or auto\) for the rule\.

## Setting Up Manual Remediation \(Console\)<a name="setup-manualremediation"></a>

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. Choose **Rules** on the left and then on the **Rules** page, choose **Add Rule** to add new rules to the rule list\. 

   For existing rules, select the noncompliant rule from the rule list and choose **Edit**\.

1. On the **Edit ***name of the rule* page, in the **Choose remediation action** section, choose the appropriate remediation action from the recommended list\.

   Depending on the selected remediation action, you see specific parameters or no parameters\.

1. \(Optional\): If you want to pass the resource ID of noncompliant resources to the remediation action, choose **Resource ID parameter**\. If selected, at runtime that parameter is substituted with the ID of the resource to be remediated\.

   Each parameter has either a static value or a dynamic value\. If you do not choose a specific resource ID parameter from the drop\-down list, you can enter values for each key\. If you choose a resource ID parameter from the drop\-down list, you can enter values for all the other keys except the selected resource ID parameter\. 

1. Choose **Save**\. The **Rules** page is displayed\.

## Setting Up Auto Remediation \(Console\)<a name="setup-autoremediation"></a>

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. Choose **Rules** on the left and then on the **Rules** page, choose **Add Rule** to add new rules to the rule list\. 

   For existing rules, select the noncompliant rule from the rule list and choose **Edit**\.

1. On the **Edit ***name of the rule* page, in the **Choose remediation action** section, choose the appropriate remediation action from the recommended list\.

   Depending on the selected remediation action, you see specific parameters or no parameters\.

1. Choose **Auto remediation** to automatically remediate noncompliant resources\.

   If a resource is still non\-compliant after auto remediation, you can set the rule to try auto remediation again\. Enter the desired retries and seconds\.
**Note**  
There are costs associated with running a remediation script multiple times\.

1. \(Optional\): If you want to pass the resource ID of noncompliant resources to the remediation action, choose **Resource ID parameter**\. If selected, at runtime that parameter is substituted with the ID of the resource to be remediated\.

   Each parameter has either a static value or a dynamic value\. If you do not choose a specific resource ID parameter from the drop\-down list, you can enter values for each key\. If you choose a resource ID parameter from the drop\-down list, you can enter values for all the other keys except the selected resource ID parameter\. 

1. Choose **Save**\. The **Rules** page is displayed\.

## Setting Up and Applying a Remediation Action Remediation Using Rules and Resources \(Console\)<a name="remediation-using-rules-resources-page"></a>

You can also set up remediation from the Rules and the Resources pages\. The following procedures provide more details about each workflow\.

### Using Rules<a name="remediation-using-console-rules"></a>

You can apply a remediation action to a noncompliant rule from **Rules** on the left\.

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. Choose **Rules** on the left and then on the **Rules** page, choose **Add Rule** to add new rules to the rule list\.

   For existing rules, select the noncompliant rule from the rule list and choose **Edit**\.

1. Choose **Manage remediation** and on the **Manage remediation: ***name of the rule* page, select the appropriate remediation action from the recommended list\. The remediation actions are related to AWS Systems Manager automation documents\.

   Depending on the selected remediation action, you will see either specific parameters or no parameters\.

1. If you want to pass the resource ID of noncompliant resources to the remediation action, choose **Resource ID parameter**\. If selected, at runtime that parameter is substituted with the ID of the resource to be remediated\.

   Each parameter has either a static value or a dynamic value\. If you do not choose a specific resource ID parameter from the drop\-down list, you can enter values for each key\. If you choose a resource ID parameter from the drop\-down list, you can enter values for all the other keys except the selected resource ID parameter\. 

1. Choose **Save**\.

1. In the **Choose resources in scope** section, choose all the noncompliant resources\. The resources in scope include those resources where this rule is applied and their compliance status\.

   For more information about a resource, choose **Resource actions** and either choose **View details**, **Configuration timeline**, or **Compliance timeline**\.

1. Choose **Remediate**\.

   If the resources are remediated, the resource compliance status is compliant\. To view the compliant resources, select **Compliant** from the compliance status list\.

   If the resources are not remediated, the action status column displays ** Action execution failed \(details\)**\. Choose **\(details\)** to view the main action steps invoked during the execution of the remediation action and the status of each action step\. 
**Note**  
For troubleshooting failed remediation actions, you can run the AWS Command Line Interface \(AWS CLI\) command `describe-remediation-execution-status` to get detailed view of a Remediation Execution for a set of resources\. The details include state, timestamps for remediation execution steps, and any error messages for the failed steps\.

### Using Resources<a name="remediation-using-console-resources"></a>

You can also apply a remediation action to a noncompliant rule from **Resources** on the left\.

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. Choose **Resources** on the left and then on the **Resource inventory** page, **Resources** is selected by default\.

1. Select one or more resources from the resource type and choose **Look up**\.

1. Choose the name of the appropriate noncompliant resource from the resource table\.

1. On the **Resource details: *** name of the resource* page, choose one or more noncompliant rules from the rules in scope\.

1. Choose **Rule actions** and select **Manage remediation**\. 

1. On the **Manage remediation: ***name of the rule* page, select the appropriate remediation action\.

   Depending on the selected remediation action, you will see either specific parameters or no parameters\.

1. If you want to pass the resource ID of noncompliant resources to the remediation action, choose **Resource ID parameter**\. If selected, at runtime that parameter is substituted with the ID of the resource to be remediated\.

   Each parameter has either a static value or a dynamic value\. If you do not choose a specific resource ID parameter from the drop\-down list, you can enter values for each key\. If you choose a resource ID parameter from the drop\-down list, you can enter values for all the other keys except the selected resource ID parameter\. 

1. Choose **Save**\.

1. In the **Choose resources in scope** section, choose all the noncompliant resources\. The resources in scope include those resources where this rule is applied and their compliance status\.

   For more information about a resource, choose **Resource actions** and either choose **View details**, **Configuration timeline**, or **Compliance timeline**\.

1. Choose **Remediate**\.

   If the resources are remediated, the resource compliance status is **compliant**\. To view the compliant resources, select **Compliant** from the compliance status list\.

   If the resources are not remediated, the action status column displays ** Action execution failed \(details\)**\. Choose **\(details\)** to view the main action steps invoked during the execution of the remediation action and the status of each action step\.
**Note**  
For troubleshooting failed remediation actions, you can run the AWS Command Line Interface \(AWS CLI\) command `describe-remediation-execution-status` to get detailed view of a Remediation Execution for a set of resources\. The details include state, timestamps for remediation execution steps, and any error messages for the failed steps\.

## Delete Remediation Action \(Console\)<a name="delete-remediation-action"></a>

To delete a rule first you must delete remediation action associated with that rule\. 

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. Choose **Rules** on the left and then on the **Rules** page, select the rule from the rule list and choose **Edit**\.

1. On the rule page, choose **Edit** again\.

1. On the **Edit ***name of the rule* page, in the **Choose remediation action** section, choose **Delete remediation action** and confirm your delete action\.
**Note**  
If remediation is in progress, the remediation action is not deleted\. If you choose **Delete remediation action**, you cannot retrieve the remediation action\. When you delete a remediation action, AWS Config does not delete a rule\.

   If the remediation action is deleted, the **Resource ID parameter** is empty and displays N/A\. On the **Rules** page, the remediation action column displays **Not set** for the corresponding rule\.

## Managing Remediation \(API\)<a name="remediate-api"></a>

### Manual Remediation<a name="remediate-api"></a>

Use the following AWS Config API actions to manage remediation:
+ [DeleteRemediationConfiguration](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteRemediationConfiguration.html)
+ [DescribeRemediationConfigurations](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeRemediationConfigurations.html)
+ [DescribeRemediationExecutionStatus](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeRemediationExecutionStatus.html)
+ [PutRemediationConfigurations](https://docs.aws.amazon.com/config/latest/APIReference/API_PutRemediationConfigurations.html)
+ [StartRemediationExecution](https://docs.aws.amazon.com/config/latest/APIReference/API_StartRemediationExecution.html)

### Auto Remediation<a name="remediate-api"></a>

Use the following AWS Config API actions to manage auto remediation:
+ [PutRemediationExceptions](https://docs.aws.amazon.com/config/latest/APIReference/API_PutRemediationExceptions.html)
+ [DescribeRemediationExceptions](https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeRemediationExceptions.html)
+ [DeleteRemediationExceptions](https://docs.aws.amazon.com/config/latest/APIReference/API_DeleteRemediationExceptions.html)