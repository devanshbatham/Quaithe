

## ShadowClone


ShadowClone enables you to execute multiple commands in parallel, turning single threaded CLI utilities into blazing fast multithreaded utilities 


## Installation

```

```


## How it works? 


ShadowClone utilizes the concurrent.futures module in Python to execute multiple commands in parallel. It creates a thread pool with a configurable number of worker processes and submits each command to the thread pool as a separate task. The thread pool manages the execution of each task, and the progress bar displays the status of each task as it executes.

## Use Case

