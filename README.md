

## ShadowClone


ShadowClone enables you to execute multiple commands in parallel, turning single threaded CLI utilities into blazing fast multithreaded utilities 


## Installation

```
git clone https://github.com/devanshbatham/ShadowClone
cd ShadowClone
chmod +x setup.sh
./setup.sh
```


## Use Cases


Suppose you have a list of domain names in a file called `domains.txt`, and you want to run the `subfinder` tool on each domain to find subdomains. However, let's assume `subfinder` is a single-threaded tool, which means that running it on each domain one at a time can be slow and inefficient. You can use the ShadowClone tool to execute `subfinder` on multiple domains in parallel, which can speed up the process significantly.

Here's an example command that demonstrates how to use ShadowClone to run `subfinder` on each domain in parallel:

```
xargs -I {} -a domains.txt echo "subfinder -d {} -o {}.txt" | shadowclone -w 30 -silent
```

In this command, `xargs` reads each domain name from the `domains.txt` file and passes it to the `echo` command as an argument. The `echo` command then outputs a command string that runs `subfinder` on the domain and saves the output to a file with the same name as the domain.

The output of `echo` is then piped to `shadowclone`, which runs each command in parallel with a maximum of 30 worker processes (`-w 30`).

By using ShadowClone to run `subfinder` on each domain in parallel, you can significantly speed up the process of finding subdomains and make better use of your system's resources.


## How it works? 


ShadowClone utilizes the concurrent.futures module in Python to execute multiple commands in parallel. It creates a thread pool with a configurable number of worker processes and submits each command to the thread pool as a separate task. The thread pool manages the execution of each task, and the progress bar displays the status of each task as it executes.



