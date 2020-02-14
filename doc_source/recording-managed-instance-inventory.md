# Recording Software Configuration for Managed Instances<a name="recording-managed-instance-inventory"></a>

You can use AWS Config to record software inventory changes on Amazon EC2 instances and on\-premises servers\. This enables you to see the historical changes to software configuration\. For example, when a new Windows update is installed on a managed Windows instance, AWS Config records the changes and then sends the changes to your delivery channels, so that you are notified about the change\. With AWS Config, you can see the history of when Windows updates were installed for the managed instance and how they changed over time\. 

You must complete the following steps to record software configuration changes:
+ Turn on recording for the managed instance inventory resource type in AWS Config\.
+ Configure EC2 and on\-premises servers as *managed instances* in AWS Systems Manager\. A managed instance is a machine that has been configured for use with Systems Manager\.
+ Initiate collection of software inventory from your managed instances using the Systems Manager Inventory capability\.

You can also use AWS Config rules to monitor software configuration changes and be notified whether the changes are compliant or noncompliant against your rules\. For example, if you create a rule that checks whether your managed instances have a specified application, and an instance doesn't have that application installed, AWS Config flags that instance as noncompliant against your rule\. For a list of AWS Config managed rules, see [List of AWS Config Managed Rules](managed-rules-by-aws-config.md)\.

**To enable recording of software configuration changes in AWS Config:**

1. Turn on recording for all supported resource types or selectively record the managed instance inventory resource type in AWS Config\. For more information, see [Selecting Which Resources AWS Config Records](select-resources.md)\.

1. Launch an Amazon EC2 instance with an instance profile for Systems Manager that includes the **AmazonSSMManagedInstanceCore** managed policy\. This AWS managed policy enables an instance to use Systems Manager service core functionality\.

   For information about other policies you can add to the instance profile for Systems Manager, see [Create an IAM Instance Profile for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-instance-profile.html) in the *AWS Systems Manager User Guide*\.
**Important**  
SSM Agent is Amazon software that must be installed on a managed instance in order to communicate with the Systems Manager in the cloud\. If your EC2 instance was created from an AMI for one of the following operating systems, the agent is preinstalled:   
Windows Server 2003\-2012 R2 AMIs published in November 2016 or later
Windows Server 2016 and 2019
Amazon Linux
Amazon Linux 2
Ubuntu Server 16\.04
Ubuntu Server 18\.04
On EC2 instances that were not created from an AMI with the agent preinstalled, you must install the agent manually\. For information, see the following topics in the *AWS Systems Manager User Guide*:   
[Installing and Configuring SSM Agent on Windows Instances](url-sys-user;sysman-install-ssm-win.html)
[Installing and Configuring SSM Agent on Amazon EC2 Linux Instances](url-sys-user;sysman-install-ssm-agent.html)

1. Initiate inventory collection as described in [Configuring Inventory Collection](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-inventory-configuring.html) in the *AWS Systems Manager User Guide*\. The procedures are the same for Linux and Windows instances\.

   AWS Config can record configuration changes for the following inventory types:
   + **Applications** – A list of applications for managed instances, such as antivirus software\. 
   + **AWS components** – A list of AWS components for managed instances, such as the AWS CLI and SDKs\.
   + **Instance information** – Instance information such as OS name and version, domain, and firewall status\.
   + **Network configuration** – Configuration information such as IP address, gateway, and subnet mask\.
   + **Windows Updates** – A list of Windows updates for managed instances \(Windows instances only\)\.
**Note**  
AWS Config doesn't support recording the custom inventory type at this time\.

Inventory collection is one of many Systems Manager capabilities, which are grouped in the categories *Operations Management*, *Actions & Change*, *Instances & Nodes*, and *Shared Resources*\. For more information, see [What is Systems Manager?](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) and [Systems Manager Capabilities](https://docs.aws.amazon.com/systems-manager/latest/userguide/features.html) in the *AWS Systems Manager User Guide*\.