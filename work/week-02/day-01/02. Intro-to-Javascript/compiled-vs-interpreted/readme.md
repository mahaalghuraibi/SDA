# Compiled vs Interpreted Languages

Understanding whether a programming language is **compiled** or **interpreted** helps explain how code is executed and why some languages behave faster than others.

---

## 1. Compiled Languages

- The **source code** you write is transformed by a **compiler** into **machine code** that the computer can execute directly.  
- Compilation happens **before the program runs**, so the computer does not translate the code line by line at runtime.  
- Examples: **C, C++, Rust, Go**

**Characteristics:**

- Faster execution because the code is already in machine code.  
- Compilation is done **once**, and the program can be run many times.  
- Errors are usually detected **at compile time**.

**Workflow:**

```
Source Code (.c/.cpp)
      |
      v
   Compiler
      |
      v
Machine Code (.exe/.out)
      |
      v
Runs on the computer
```

---

## 2. Interpreted Languages

- The **source code** is read and executed **line by line** by an **interpreter** at runtime.  
- No separate machine code file is generated beforehand.  
- Examples: **Python, JavaScript (traditional engines), Ruby**

**Characteristics:**

- Easier to test and modify code quickly.  
- Slower execution because translation happens **while the program runs**.  
- Errors appear **at runtime**.

**Workflow:**

```
Source Code (.py/.js)
      |
      v
   Interpreter
      |
      v
Executes line by line
```

---

## 3. Hybrid Approaches

Some languages use a combination of compilation and interpretation:

- **Java**: Source code → compiled to **bytecode** → JVM interprets or JIT compiles at runtime.  
- **JavaScript (modern engines like V8)**: Interpreted first, then optimized to machine code using **Just-In-Time (JIT) compilation**.

---

## 4. Key Differences

| Feature | Compiled | Interpreted |
|---------|----------|-------------|
| Translation | Entire program before execution | Line by line at runtime |
| Speed | Generally faster | Generally slower |
| Errors | Detected at compile time | Detected at runtime |
| Output | Machine code / executable file | No separate file, executed by interpreter |
| Examples | C, C++, Rust, Go | Python, Ruby, JavaScript |

---

## Summary

- **Compiled languages:** Translate all code to machine code **before** running → faster execution, catches errors early.  
- **Interpreted languages:** Translate code **while running** → flexible, easier to debug, but generally slower.  

Understanding this distinction helps students **predict performance**, **debug effectively**, and **choose the right language for a task**.
