from database import Database
from cli2 import BookCLI
from bookModel import BookModel

db = Database(database="Rel5", collection="livros")
bookModel = BookModel(database=db);

bookCLI = BookCLI(bookModel);
bookCLI.run();
