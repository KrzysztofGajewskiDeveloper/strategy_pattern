# strategy_pattern
Strategy Design Pattern Simplified Example, pythonic version

**CLASSIC STRATEGY DESIGN PATTERN:**
The Strategy design pattern is a behavioral design pattern that enables the definition of a family of interchangeable strategies (strategy interface) and encapsulates each one as a separate class (strategy class). It allows the algorithms (strategies) to be selected at runtime and used interchangeably based on the specific context or requirements. The Strategy pattern is typically useful when there are multiple behaviors that need to be dynamically selected.


**PYTHONIC VERSION OF STRATEGY DESIGN PATTERN:**

Using first-class functions (functions that can be passed as arguments to functions, returned by functions, and stored in data structures), allows for more flexibility and dynamic behavior changes without modifying the existing code. Instead of creating separate classes for each strategy, different strategies can be implemented as separate functions.
 
strategy_pattern.py demonstrates in a pythonic version of the Strategy Design Pattern: The example focuses on generating and saving reports in different formats based on the chosen strategy.

typing.**Callable** is imported to define the Alias/**Interface** for the strategy functions.

```python
ReportSaverStrategy = Callable[[str], None]

comma_csv_strategy: ReportSaverStrategy = partial(save_as_csv, delimiter=',')
encrypted_pdf_strategy: ReportSaverStrategy = partial(save_as_pdf, encryption=True)
decrypted_pdf_strategy: ReportSaverStrategy = partial(save_as_pdf, encryption=False)
