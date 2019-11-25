# Introduction to GCP self-paced workshop

**1. Making sure everything is setup**

- You should register with your isae-supaero email using the link sent by Dennis
- This should lead you to have a google cloud platform project open with some credits

**2. My First Google Compute Engine Instance**

- Follow this codelab: https://codelabs.developers.google.com/codelabs/cloud-create-a-vm
- Try to create an "n1-standard-2" instance with ubuntu-18.04 as a base image

To go further:
https://cloud.google.com/compute/docs/instances/

**3. Connecting to an instance usng SSH**

- Keep an instance (for example the last you created) open and note its public IP address
- [Generate an SSH key](https://www.ssh.com/ssh/keygen/) in cloud shell / your machine
- [Add the public key to the SSH metadata of Google Compute Engine](https://cloud.google.com/compute/docs/instances/adding-removing-ssh-keys)
- Connect to the instance with your key: `ssh user@instance-ip`
- If you are on cloud shell or have gcloud installed you can do `gcloud compute ssh instance-name` as well. NOTE THIS WILL
- Verify that you are on the remote machine (check terminal, or `ifconfig`)
- Execute "echo 'hello world'" on the remote [instance without opening a session first (`ssh --command ...`)](https://www.cyberciti.biz/faq/unix-linux-execute-command-using-ssh/)

To go further:
https://gravitational.com/blog/ssh-handshake-explained/

**4. Detachable Sessions using tmux**

- **if you are on google cloud shell DISABLE TMUX using settings/tmux/disable**
- Connect to your instance using SSH
- Question: What happens if you start a long computation and disconnect ? 
- Check that tmux is installed on the remote instance (run `tmux`). if not [install it](https://computingforgeeks.com/linux-tmux-cheat-sheet/)
- Follow this tutorial: https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/
- To check you have understood you should be able to:
    - Connect to your remote instance with ssh
    - Start a tmux session
    - Launch a process (for example `top`) inside it
    - Detach from the session (`CTRL+B :detach`)
    - Kill the ssh connection
    - Connect again
    - `tmux attach` to your session
    - Your process should still be here !

Congratulations :) 

## 4. Google Cloud Storage

- Follow this codelab: https://codelabs.developers.google.com/codelabs/es003l-storage/#0
- Follow this codelab: https://codelabs.developers.google.com/codelabs/cloud-upload-objects-to-cloud-storage
- From your remote instance, follow those tutorials while using only `gsutil` https://cloud.google.com/storage/docs/how-to

## 5. Intro to Infrastructure as code

- Create an GCE instance without using the UI using this tutorial: https://cloud.google.com/compute/docs/instances/create-start-instance#publicimage

Welcome to the world of scripting instance creations ! 

- In google cloud shell, use the file editor and the shell to run the tutorial for the Deployment Manager
https://cloud.google.com/deployment-manager/docs/quickstart

Welcome to the world of Infrastructure as Code
