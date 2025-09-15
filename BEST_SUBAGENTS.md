## Riassunto e Istruzioni dal Video "The MOST Incredible Use of Claude Code Sub-Agents"

Questo documento riassume i concetti chiave presentati nel video e riporta fedelmente le istruzioni vocali fornite dall'autore come esempi di prompt per istruire agenti AI a risolvere problemi complessi.

### Punti Salienti del Video

Il concetto centrale del video si basa su uno studio chiamato **ParaThinker**, il quale ha scoperto un fenomeno definito "visione a tunnel" (tunnel vision) nei modelli linguistici. Questo accade quando i primi passi iniziali di un modello lo bloccano in un percorso di ragionamento non ottimale, rendendo inefficaci anche budget di "pensiero" molto ampi (come la funzione `ultrathink` di Claude).

1.  **Il Problema della "Visione a Tunnel"**: Un singolo agente, anche con molte risorse, può rimanere bloccato in un approccio sbagliato fin dall'inizio. Aumentare le risorse (più token per pensare) produce rendimenti decrescenti.

2.  **La Soluzione: Percorsi di Ragionamento Paralleli**: Lo studio dimostra che addestrare un modello a generare percorsi di ragionamento multipli e indipendenti per lo stesso problema porta a risultati significativamente migliori. È un approccio "divide et impera" applicato al ragionamento.

3.  **Implementazione Pratica con Sub-Agenti**: Dato che non è possibile ri-addestrare modelli chiusi come Claude, l'autore adotta un approccio ispirato allo studio: utilizzare un **agente orchestratore** che delega il problema a più **sub-agenti**.

4.  **Il Metodo della "Maggioranza"**: L'agente principale (orchestratore) genera un numero definito di sub-agenti (es. 8), ognuno incaricato di risolvere lo stesso problema seguendo una **strategia diversa e unica**. L'orchestratore analizza le soluzioni proposte e implementa quella suggerita dalla maggioranza dei sub-agenti.

5.  **Caso di Studio Reale**: L'autore applica questo metodo per risolvere un bug reale nella sua applicazione mobile: uno scroll orizzontale che si resetta da solo. Dimostra prima il fallimento dell'approccio `ultrathink` (un singolo agente con massime risorse) e poi il successo dell'approccio con 8 sub-agenti, che risolve il bug correttamente.

6.  **Conclusione**: Questa tecnica non è da usare sempre a causa dell'elevato consumo di token, ma si rivela uno strumento estremamente potente per problemi molto complessi dove gli approcci tradizionali falliscono.

---

### Istruzioni Vocali per l'Agente

Queste sono le trascrizioni esatte dei comandi vocali che l'autore fornisce nel video per istruire i suoi agenti.

#### 1. Istruzione per il Sub-Agente Analista (`strategy-analyzer`)

Questo prompt definisce il comportamento del sub-agente. La sua funzione non è modificare il codice, ma solo analizzare il problema secondo la strategia assegnata e proporre una conclusione teorica.

> "Hey, so basically I want you to solve the problem that's been given to you following the strategy that like you were told to follow. Don't make changes to the code at all, just follow the strategy, think through how you would solve the problem, don't make changes, and then just give a conclusion of how it would be solved using that strategy."

#### 2. Istruzione per l'Agente Standard (Caso di Controllo con `ultrathink`)

Questo è il prompt usato per il test fallimentare, dove un singolo agente deve risolvere il problema dello scroll.

> "Hey, so basically the problem is that currently on the homepage of the mobile application, when I switch to a different category after like scrolling horizontally, then it automatically goes back to the beginning of all the categories. Like the horizontal scroll resets to the very beginning. How do you fix this? After coming up with a solution, implement that particular fix."

#### 3. Istruzione per l'Agente Orchestratore (che userà i Sub-Agenti)

Questo è il prompt chiave che istruisce l'agente principale a non risolvere il problema da solo, ma a delegarlo a 8 sub-agenti, ognuno con una strategia unica, per poi implementare la soluzione di maggioranza.

> "Hey, so basically you should implement not do this yourself. You should get eight different versions of the @strategy-analyzer subagent to do this for you on your behalf. And then you should look at the majority solutions and then implement the majority like solution. Each subagent that you spawn should be given a different strategy to follow in regards to solving the problem. No two subagents should follow the same strategy."
