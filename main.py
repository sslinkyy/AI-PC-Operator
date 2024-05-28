if __name__ == "__main__":
    task_manager = TaskManagerWithErrorHandling()
    task_manager.execute_task("analyze_stock AAPL")
    task_manager.execute_task("make_trade AAPL")
    
    # Simulating an error scenario
    try:
        # This will throw an error since the command is not known
        task_manager.execute_task("unknown_command")
    except Exception as e:
        task_manager.execute_task(f"handle_error: {str(e)}")
