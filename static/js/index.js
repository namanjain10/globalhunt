// alert ('ygshs');

$('#first').submit (function () {
  if ($('input[name=canId]').val() == ('')) {
    event.preventDefault();
    alert ('Can Id cant be empty!!');
  }
  else if ($('input[name=email\\@primary]').val() == ('')) {
    event.preventDefault();
    alert ('Primary email Id cant be empty!!');
  }
  else if ($('input[name=email\\@secondary]').val() == ('')) {
    event.preventDefault();
    alert ('Secondary email Id cant be empty!!');
  }
  else if ($('input[name=email\\@third]').val() == ('')) {
    event.preventDefault();
    alert ('Third email Id cant be empty!!');
  }
  else if ($('input[name=email\\@fourth]').val() == ('')) {
    event.preventDefault();
    alert ('Fourth email Id cant be empty!!');
  }
  else if ($('input[name=email\\@fifth]').val() == ('')) {
    event.preventDefault();
    alert ('Fifth email Id cant be empty!!');
  }
})
