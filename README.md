# snp
## About
SNP software to analyze and annotate variant files

## Contribute
In order to contribute to the developement of the **snp* software repository: 
1. Fork the Git repository to your own account:
    1. Go to https://github.com/bredeson/snp
    2. Click the `Fork` button in the upper-right corner of the browser.
    3. Press the green `Create Fork` button at the bottom of the **Create a new fork** page. You will then be sent to your newly-forked GitHub repository. 
  
2. Clone your newly-forked Git repository to your local machine:
    1. Press the green `Code` button. You'll be presented with possible cloning path options.
    2. Click the *SSH* tab.
    3. Copy the path by pressing the overlapping squares icon to the right of the repo URL, or highlight the text and press `command + C`.
    4. In your Terminal application, type and execute the command below. **NOTE**: replace `<git-path>` below the repo URL you copied above.
      ```bash
      git clone <git-path> 
      ```
    
3. Configure your forked and cloned Git repository on your local machine with an `upstream` remote:
    1. Change directory into the newly-cloned *snp* repo:
      ```bash
      cd snp
      ```
    
    2. Add the `upstream` remote to https://github.com/bredeson/snp:
      ```bash
      git remote add upstream https://github.com/bredeson/snp.git
      ```
    
4. Next, `add` and `commit` your changes as you would normally, **but don't push your changes yet!** First, do:
    ```bash
    git pull upstream main
    ```
    
5. Now, push your changes to your `origin` repo:
    ```bash
    git push origin main
    ```
    
6. Submit a **Pull Request**:
    1. In your browser, go to *your* forked Git repository.
    2. Click on the *Pull requests* tab.
    3. Click the green `New pull request` button.
    4. Click the green `Create pull request` button.
    5. Add in sucinct Title and descriptive summary of the changes you made.
    6. Click the green `Create pull request` button.
