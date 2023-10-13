import re

class SQLValidator:

    def __init__(self, script):
        self.script = script
        self.naming_rules = {
            'task_search':r"(?is)(CREATE\s+TASK\s+|CREATE\s+OR\s+REPLACE\s+TASK)\s+\w+_000_COD\."
            , 'task_name': r'(?is)TSK_[A-Za-z0-9_]*'
            , 'proc_search': r"(?is)(CREATE\s+PROCEDURE\s+|CREATE\s+OR\s+REPLACE\s+PROCEDURE)\s+\w+_000_COD\."
            , 'proc_name': r'(?is)PRC_[A-Za-z0-9_]*'
            }

    def check_tasks(self):

        task_search = self.naming_rules['task_search']
        task_name = self.naming_rules['task_name']
        
        # Read in .sql script
        with open(self.script, 'r') as file:

            # Search for any task DDL
            search_for_tasks = re.search(task_search, file.read(), re.IGNORECASE | re.DOTALL)

            # If task name doesn't match regex pattern then they are named incorrectly
            if search_for_tasks:
                search_for_naming = re.search(task_name, open(self.script, 'r').read(), re.IGNORECASE | re.DOTALL)

                if not search_for_naming:
                    raise Exception('\u2613 FAIL: incorrect naming convention for task. Task name must be prefixed with TSK_')
                else:
                    return f"\u2714 PASS: '{search_for_naming.group(0)}' follows naming convention"
            else:
                pass

    def check_procs(self):

        proc_search = self.naming_rules['proc_search']
        proc_name = self.naming_rules['proc_name']
        
        # Read in .sql script
        with open(self.script, 'r') as file:

            # Search for any task DDL
            search_for_procs = re.search(proc_search, file.read(), re.IGNORECASE | re.DOTALL)

            # If task name doesn't match regex pattern then they are named incorrectly
            if search_for_procs:
                search_for_naming = re.search(proc_name, open(self.script, 'r').read(), re.IGNORECASE | re.DOTALL)

                if not search_for_naming:
                    raise Exception('\u2613 FAIL: incorrect naming convention for prcoedure. Procedure name must be prefixed with PRC_')
                else:
                    return f"\u2714 PASS: '{search_for_naming.group(0)}' follows naming convention"
            else:
                pass
