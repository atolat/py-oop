# Single Responsibility Principle
# - Separation of Concerns
# - Do not overload class with too many responsibilities
# - A class should have a single reason to change and that change should be related to it's primary responsiobility

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    # break SRP -
    # These features might be common for a number of applications and require a central implementation 
    # that can be changed in the future, implement it as a different class.
    def save(self, filename):
        file = open(filename, "w")
        file.write(str(self))
        file.close()

    def load(self, filename):
        pass

    def load_from_web(self, uri):
        pass

# Follows SRP


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug.")
print(f"Journal entries:\n{j}\n")

p = PersistenceManager()
file = r'./temp.txt'
p.save_to_file(j, file)

# verify!
with open(file) as fh:
    print(fh.read())
