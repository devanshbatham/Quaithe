<h2 align="center">ShadowClone ⚡️</h2>

<p align="center">ShadowClone empowers you to execute multiple commands in parallel for blazing-fast performance.</p>


<p align="center">
  <a href="#installation">🏗️ Installation</a>
  <a href="#use-cases">📚 Use Cases</a>
  <a href="#usage">⛏️ Usage</a>
  <a href="#how-it-works">🔧 How it works?</a>
  <br>
</p>


## Installation

```sh
git clone https://github.com/devanshbatham/ShadowClone
cd ShadowClone
chmod +x setup.sh
./setup.sh
```


## Use Cases

Suppose you have a list of domain names in a file called `domains.txt`, and you want to run the `subfinder` tool on each domain to find subdomains. However, let's assume `subfinder` is a single-threaded tool, which means that running it on each domain one at a time can be slow and inefficient. You can use the ShadowClone tool to execute `subfinder` on multiple domains in parallel, which can speed up the process significantly.

Here's an example command that demonstrates how to use ShadowClone to run `subfinder` on each domain in parallel:

```sh
xargs -I {} -a domains.txt echo "subfinder -d {} -o {}.txt" | shadowclone -w 30 -silent
```

In this command, `xargs` reads each domain name from the `domains.txt` file and passes it to the `echo` command as an argument. The `echo` command then outputs a command string that runs `subfinder` on the domain and saves the output to a file with the same name as the domain.

The output of `echo` is then piped to `shadowclone`, which runs each command in parallel with a maximum of 30 worker processes (`-w 30`).

By using ShadowClone to run `subfinder` on each domain in parallel, you can significantly speed up the process of finding subdomains and make better use of your system's resources.


## Usage

The ShadowClone tool takes a list of commands to execute on standard input (stdin). Each command should be on a separate line.


```sh
cat commands.txt | shadowclone -w 10 -silent
```

In this command, `cat` reads a list of commands from a file called `commands.txt` and passes them to ShadowClone on standard input. ShadowClone runs each command in parallel with a maximum of 10 worker processes (`-w 10`). The `-silent` flag tells ShadowClone not to print the output of each command to the console.

Note that each command should be a complete shell command, including any arguments or options.


## How it works?

ShadowClone utilizes the concurrent.futures module in Python to execute multiple commands in parallel. It creates a thread pool with a configurable number of worker processes and submits each command to the thread pool as a separate task. The thread pool manages the execution of each task, and the progress bar displays the status of each task as it executes.
```
