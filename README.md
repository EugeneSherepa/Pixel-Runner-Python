Де я можу відобразити цей код?
flowchart TD
    Start([Початок]) --> Init[Ініціалізація локалізації<br>та кодування консолі]
    
    Init --> CreateExo[Створення 10 екзофреймів<br>EF1...EF10<br>OSFrame]
    
    CreateExo --> InitSets[Ініціалізація порожніх множин<br>setA та setB<br>FrameSet]
    
    InitSets --> FillA[Наповнення множини A:<br>addFrame EF1, EF2, EF3, EF4,<br>EF5, EF7, EF9, EF10]
    
    FillA --> FillB[Наповнення множини B:<br>addFrame EF1, EF3, EF4, EF6,<br>EF7, EF8, EF9, EF10]
    
    FillB --> DisplaySets[/Виведення таблиць<br>складу множин A та B/]
    
    DisplaySets --> OpUnion[Виконання операції ОБ'ЄДНАННЯ:<br>setUnion = setA ∪ setB]
    
    OpUnion --> DispUnion[/Виведення результату<br>об'єднання/]
    
    DispUnion --> OpInter[Виконання операції ПЕРЕТИНУ:<br>setIntersection = setA ∩ setB]
    
    OpInter --> DispInter[/Виведення результату<br>перетину/]
    
    DispInter --> OpDiffAB[Виконання операції РІЗНИЦІ A \ B:<br>setDifferenceAB = setA \ setB]
    
    OpDiffAB --> DispDiffAB[/Виведення результату<br>різниці A \ B/]
    
    DispDiffAB --> OpDiffBA[Виконання операції РІЗНИЦІ B \ A:<br>setDifferenceBA = setB \ setA]
    
    OpDiffBA --> DispDiffBA[/Виведення результату<br>різниці B \ A/]
    
    DispDiffBA --> End([Кінець])

    style Start fill:#f9f,stroke:#333,stroke-width:2px
    style End fill:#f9f,stroke:#333,stroke-width:2px
    style DisplaySets fill:#ff9,stroke:#333,stroke-width:2px
    style DispUnion fill:#ff9,stroke:#333,stroke-width:2px
    style DispInter fill:#ff9,stroke:#333,stroke-width:2px
    style DispDiffAB fill:#ff9,stroke:#333,stroke-width:2px
    style DispDiffBA fill:#ff9,stroke:#333,stroke-width:2px
