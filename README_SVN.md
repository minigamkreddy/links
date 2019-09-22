Subversion is a free/open source version control system (VCS).
That is, Subversion manages files and directories, and the changes made to them, over time.
This allows you to recover older versions of your data, or examine the history of how your data changed.
In this regard, many people think of a version control system as a sort of “time machine.” 

Basic Usage

    Procedure to checkout project/Repo

    $ svn checkout http://172.16.2.19/svn/Onelink_Connect
                      (or)
    $ svn co http://172.16.2.19/svn/Linux_Kernel_Capability

    Procedure to check-in updated Repo

To check-in the files first we have to add the files and after that we have to commit in to the server.

Before adding the files in SVN folder you have to use the 'SVN up' or 'SVN update' to get the recent modifications.

    Commands to add & commit the files 

    $ svn add filename

no need to add the file every time, once you have added the file. You can directly commit the files after modifications.

    $ svn commit -m "proper message"
                 (or)
    $ svn ci -m "proper message"

    Command to lock a file with example 

Lock worksvn lock TARGETing copy paths or URLs in the repository so that no other user can commit changes to them.

     $ svn lock FILES

Examples

Lock two files in your working copy:

$ svn lock tree.jpg house.jpg
'tree.jpg' locked by user 'harry'.
'house.jpg' locked by user 'harry'.

Lock a file in your working copy that is currently locked by another user:

$ svn lock tree.jpg
svn: warning: W160035: Path '/tree.jpg is already locked by user 'sally' in filesystem '/var/svn/repos/db'
$ svn lock --force tree.jpg
'tree.jpg' locked by user 'harry'.

Lock a file without a working copy:

$ svn lock http://172.16.2.19/svn/Onelink_Connect/Project_Management/Software%20Project%20Plan/GES-Project-Scrum_Sheet-Onelink_Connect.xls
'GES-Project-Scrum_Sheet-Onelink_Connect.xls' locked by user 'harry'.

Note: Files will be automatically unlocked when committed by locked user

Use SVN unlock for unlocking

$ svn unlock FILES

