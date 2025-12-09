# JOB SCHEDULER PROJECT

from bst_structure import *

run_status = True

my_company = BinarySearchTree()


def welcome():
    print("Welcome to your job scheduler app!")
    print("To get started:")
    print("\t1: Check current job schedule")
    print("\t2: Add a job to the schedule")
    print("\t3: Delete a job from the schedule")
    print("\t4: Quit job scheduler and review jobs")


def job_schedule():
    my_company.job_order()


def add_job():
    job_title = input("Enter the name of the job: ")
    job_start_time = input("Enter the start time of the job in the following format (hh:mm:ss): ")
    job_duration = input("Enter the duration of the job: ")
    job_information = f"{job_start_time},{job_duration},{job_title}"

    my_company.insert_job(f"{job_information}")


def delete_job():
    job_to_delete = input("Enter the name of the job: ")
    my_company.delete_job(job_to_delete)


def exit_app():
    global run_status
    run_status = False
    print("\nThanks for using the app, hope to see you soon!")
    print("Here are your final scheduled jobs:")
    my_company.job_order()


def get_input():
    while True:
        user_input = input("Enter a number (1–4): ").strip()

        if not user_input.isdigit():
            print("Invalid input — please enter a number.")
            continue

        option = int(user_input)

        if option == 1:
            job_schedule()
        elif option == 2:
            add_job()
        elif option == 3:
            delete_job()
        elif option == 4:
            exit_app()
            return
        else:
            print("Please enter a valid option (1–4).")


if __name__ == "__main__":
    welcome()
    while run_status:
        get_input()