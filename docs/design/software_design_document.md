Software Design Document - Milestone 2

1. Class Diagram
```commandline
Class Diagram Code:
@startuml

' main program
class JobScheduler {
    - bst : BinarySearchTree
    + addJob(name, start, duration)
    + deleteJob(name)
    + viewJobs()
    + run()
}

' data structures
class BinarySearchTree {
    - root : Node
    + insertJob(jobInfo)
    + deleteJob(name)
    + jobOrder()
}

class Node {
    - name : String
    - startTime : DateTime
    - duration : DateTime
    - endTime : DateTime
    - left : Node
    - right : Node
}

' relationships
JobScheduler --> BinarySearchTree
BinarySearchTree --> Node

@enduml

```
2. Design Principles Analysis

3. Future Requirement Changes
Change 1: Recurring Jobs - Soemtimes the user might want to requeue jobs that they have added in the past. current design does not handle this feature well since the user has to re-add their tasks manually each time. BST insertion logic would need major updates.
Change 2: Priority Based Scheduling - If a job has a higher priority than another job, I feel like the user should be able to use the program in a way that accounts for this and rebalances the BST. The Design solely groups jobs with start and end time and doesn't accont for which jobs mgiht be more important tot he user.
Change 3: Swithching the tree structure - This would invovle replacing the BST entirely. We could try something like a AVL tree and re-evaluate the performance and practicality of this structure for the user.
Change 4: Changing UI to Graphical (GUI) - Presentation Layer can be replaced cleanly while keeping the Domain layer the same. This would help the user find it easier to use the system and make things easier to udnerstand overall. Currently I use a CLI to handle everything which isn't ideal.
Change 5. Adding a metric system - This would help to track statistics related with the user and evaluate how well they are using the system. This could help us developers when deciding whether the system is doing its job and help to optimize each part of the system.
4. Violations