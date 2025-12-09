from datetime import *


class Node:  # Node object is a job with a start time, length of the job, and name of the job

    def __init__(self, raw_info):
        raw_start, raw_length, raw_name = raw_info.split(",")
        # Original UI fields
        self.name = raw_name
        self.ui_start = raw_start
        self.ui_len = raw_length

        # Children pointers
        self.left_child = None
        self.right_child = None

        # Parse start time
        self.start_dt = datetime.strptime(raw_start, "%H:%M:%S")

        # Convert UI duration → datetime → timedelta
        d_obj = datetime.strptime(raw_length, "%H:%M:%S")
        self.length_td = timedelta(
            hours=d_obj.hour,
            minutes=d_obj.minute,
            seconds=d_obj.second
        )

        # Compute end time and trim string
        computed_end = self.start_dt + self.length_td
        self.end_str = str(computed_end)[11:]


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert_job(self, job_info):
        node = job_info if isinstance(job_info, Node) else Node(job_info)

        if self.root is None:
            self.root = node
            return

        self._insert_node(self.root, node)

    def _insert_job(self, curr, new_node):  # Current node, What to insert
        # NOTE: JOB DURATION HAS TO BE LESS THAN 24 HOURS
        c_start_hr = curr.ui_start[:2]
        c_end_hr = curr.end_str[:2]

        n_start_hr = new_node.ui_start[:2]
        n_end_hr = new_node.end_str[:2]
        if c_start_hr.startswith("0"):
            c_start_hr = c_start_hr[1]
        if c_end_hr.startswith("0"):
            c_end_hr = c_end_hr[1]
        if n_start_hr.startswith("0"):
            n_start_hr = n_start_hr[1]
        if n_end_hr.startswith("0"):
            n_end_hr = n_end_hr[1]

        c_start_hr = int(c_start_hr)
        c_end_hr = int(c_end_hr)
        n_start_hr = int(n_start_hr)
        n_end_hr = int(n_end_hr)

        # Case 1: goes to right subtree
        if n_start_hr > c_end_hr:
            if curr.right_child is None:
                curr.right_child = new_node
            else:
                self._insert_node(curr.right_child, new_node)
            return

        # Case 2: goes to left subtree
        if (n_end_hr < c_start_hr) and (n_end_hr < c_end_hr):
            if curr.left_child is None:
                curr.left_child = new_node
            else:
                self._insert_node(curr.left_child, new_node)
            return

        # Case 3: equal hour — check minutes
        if n_start_hr == c_end_hr:
            new_min = int(new_node.ui_start[3:5])
            curr_end_min = int(curr.end_str[3:5])

            if new_min > curr_end_min:
                if curr.right_child is None:
                    curr.right_child = new_node
                else:
                    self._insert_node(curr.right_child, new_node)
                return

            end_min_new = int(new_node.end_str[3:5])
            curr_start_min = int(curr.ui_start[3:5])

            if end_min_new < curr_start_min:
                if curr.left_child is None:
                    curr.left_child = new_node
                else:
                    self._insert_node(curr.left_child, new_node)
                return

        # Default conflict
        print("Your job cannot be inserted due to a time conflict with:")
        print(f"{curr.name} ({curr.ui_start})")


    def job_order(self):
        self._job_order(self.root)

    def _job_order(self, current_job_node):
        if current_job_node:
            self._job_order(current_job_node.left_child)
            print(f"|Jb Name: {current_job_node.name} | Starting Time: {current_job_node.ui_starting_time} | Duration: {current_job_node.ui_duration} |", end=" " + "\n")
            self._job_order(current_job_node.right_child)

    def min_right_subtree(self, curr):
        if curr.left_child is None:
            return curr
        else:
            return self.min_right_subtree(curr.left_child)

    def delete_job(self, active_node):
        self._delete_job(self.root, None, None, active_node)

    def _delete_job(self, current_node, prev_node, is_left, delete_node):
        if current_node:
            if delete_node == current_node.name:
                if current_node.left_child and current_node.right_child:
                    min_child = self.min_right_subtree(current_node.right_child)
                    current_node.name = min_child.data
                    self._delete_job(current_node.right_child, current_node, False, min_child.data)
                elif current_node.left_child is None:
                    if prev_node:
                        if is_left:
                            prev_node.left_child = current_node.right_child
                        else:
                            prev_node.right_child = current_node.right_child
                    else:
                        self.root = current_node.right_child
                elif current_node.left_child is None and current_node.right_child is None:
                    if prev_node:
                        if is_left:
                            prev_node.left_child = None
                        else:
                            prev_node.right_child = None
                    else:
                        self.root = None
                
                else:
                    if prev_node:
                        if not is_left:
                            prev_node.right_child = current_node.left_child
                            
                        else:
                            prev_node.left_child = current_node.left_child
                    else:
                        self.root = current_node.left_child
            elif delete_node < current_node.name:
                self._delete_job(current_node.left_child, current_node, True, delete_node)
            elif delete_node > current_node.name:
                self._delete_job(current_node.right_child, current_node, False, delete_node)
        else:
            print(f"{delete_node} not found in tree")
