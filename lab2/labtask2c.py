
class ClassroomAgent:
    def __init__(self, previous_mode="IDLE"):
        self.previous_mode = previous_mode

    def act(self, temp, occupied):
        if not occupied:
            target_mode = "ECO"
        elif temp > 26:
            target_mode = "COOL"
        elif temp < 20:
            target_mode = "WARM"
        else:
            target_mode = "IDLE"
        previous_mode = self.previous_mode
        send_command = target_mode != previous_mode
        if send_command:
            self.previous_mode = target_mode

        return previous_mode, target_mode, send_command

agent = ClassroomAgent(previous_mode="IDLE")
percepts = [
    (29, True),
    (29, True),
    (20, True),
    (26, True),
    (19, True),
    (29, False),
    (29, False)
]

print("Step | Previous | Percept | Target | Command")
print("-" * 55)
for step, (temp, occupied) in enumerate(percepts, 1):
    previous, target, send = agent.act(temp, occupied)
    if send:
        result = "SEND COMMAND"
    else:
        result = "NO COMMAND"
    print(
        step, "|",
        previous, "|",
        (temp, occupied), "|",
        target, "|",
        result
    )
