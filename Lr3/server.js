let express = require('express');
let routes  = require('./routes');
let app     = express();

app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.use('/', routes);

let PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server listening at http://localhost:${PORT}`);
});
