<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Page1</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
</head>
<body>
<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo03" aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <a class="navbar-brand" href="#">Navbar</a>
    <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled">Disabled</a>
        </li>
      </ul>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>
<a href="page2.html" target="_blank">Ссылка на страницу 2</a>
<p>
Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam aperiam blanditiis culpa dolorum facilis fuga hic id
itaque laudantium molestias placeat quaerat voluptas, voluptate. Amet deleniti dolore quidem quos ratione.
</p>
<form action="">
    <label for="field_1" class="lead">Введите ваше имя:</label>
    <input type="text" id="field_1" class="form-control form-control-lg"><br>
    <label for="field_2" class="lead">Чек-бокс:</label>
    <input type="checkbox" id="field_2" class="form-check-input"><br>
    <label for="field_3" class="lead">Введите ваш пароль:</label>
    <input type="password" id="field_3" class="form-control form-control-sm"><br>
    <textarea></textarea>
    <input type="button" value="Отправить форму" class="btn btn-primary">
</form>
</body>
</html>
