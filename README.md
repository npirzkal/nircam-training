# NIRCam GitHub Training Repository

This repository contains fake code that can be used to practice GitHub commands and
workflows. This repository is purely for training purposes. 



### Recommended instructions for contributing code to a repo:

1. Click the "Fork" button in the top right corner of this page to create a fork off of the `nircam-training` repository.
2. Make a local clone of your fork (click the green "Clone" button).
   * using SSH (`git clone git@github.com:<your_username>/nircam-training.git`)
   * using HTTPS (`git clone https://github.com/<your_username>/nircam-training.git`)
3. Change directories to the `nircam-training` directory: `cd nircam_calib`
4. Run the setup script: `python setup.py install`
5. Make sure your fork is pointing to the right places: `git remote -v`  You should see:

    `origin	git@github.com:<your_username>/nircam-training.git (fetch)`

    `origin	git@github.com:<your_username>/nircam-training.git (push)`

    If that is not what you see, type: 
    
    `git remote set-url origin git@github.com:<your_username>/nircam_calib.git`. 
    
6. Make sure your fork is pointing upstream properly by typing: 

    `git remote add upstream git@github.com:spacetelescope/nircam_calib.git`

    You should see:

    `upstream	git@github.com:spacetelescope/nircam-training.git (fetch)`

    `upstream	git@github.com:spacetelescope/nircam-training.git (push)`

7. Create a branch on your personal fork: `git checkout -b <branch_name>`
8. Make your software changes and then stage them: `git add changed_file.py`
9. Commit your new file with a description of the change: `git commit -m "Made a change"`
10. Push that branch to your personal GitHub repository (i.e. `origin`): 

    `git push origin <branch_name>`

11. On the `spacetelescope` `nircam-training` repository, create a pull request to merge your changes into `spacetelescope:master`.
12. Assign a reviewer from the team for the pull request.
13. Delete your local copy of your branch.


## Current Admins
- Bryan Hilbert [@bhilbert4](https://github.com/bhilbert4)
- Alicia Canipe [@aliciacanipe](https://github.com/aliciacanipe)
