# 6 Story Structure

The story structure has seven main chapters or parts, each of which is illustrated by the activity diagrams below. Within each diagram, the structure is broken down by major activities or quests the player must complete to beat the game. Note that as a result of branching narrative, Part 7 has two subparts. Also note that between quests, the PC generally has an unlimited amount of time to explore unlocked levels or locations.

## 6.1 Part 1: Escape from Prison Darkhenge

Prison Darkhenge is where the game starts. The PC wakes up one day, and the door to the cell is mysteriously open. The PC exits the prison and must find a key to unlock the uppermost door of the prison.

<figure markdown="block">
<figcaption>Figure 1: Activity diagram for escaping from Prison Darkhenge</figcaption>

```mermaid
flowchart LR
    S{{"START<br>Wake up from drugged state to find<br>prison cell door mysteriously open"}} --> A[Find spear] --> B[Slay creep] --> C[Get key] --> D[Exit prison] --> F((FINISH))
```

</figure>

## 6.2 Part 2: Get assassination quest from Emperor

After escaping from the prison, the PC emerges into the palace bailey to find a squadron of soldiers waiting for him. They escort the PC to Emperor Marcus, who then gives the PC the quest to assassinate Samuel the Healer, the living leader of the Calydonians, in exchange for the freedom of the PC and the PC’s sister.

<figure markdown="block">
<figcaption>Figure 2: Activity diagram for getting quest from Emperor Marcus</figcaption>

```mermaid
flowchart TB
    subgraph row1 [" "]
        direction LR
        S{{"START<br>Emerge from prison to meet<br>a squadron of soldiers"}} --> A[Meet Damien Carth] --> B[Meet Emperor] --> C[Get quest]
    end
    subgraph row2 [" "]
        direction RL
        D[See sister] --> E[Get first lead] --> G[Exit palace] --> F((FINISH))
    end
    row1 --> row2
    style row1 fill:none,stroke:none
    style row2 fill:none,stroke:none
```

</figure>

## 6.3 Part 3

<span class="redacted">Redacted</span>

## 6.4 Part 4

<span class="redacted">Redacted</span>

## 6.5 Part 5

<span class="redacted">Redacted</span>

## 6.6 Part 6

<span class="redacted">Redacted</span>

## 6.7 Part 7

<span class="redacted">Redacted</span>
