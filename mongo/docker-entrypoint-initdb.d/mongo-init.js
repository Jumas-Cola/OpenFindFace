let error = true;

let res = [
  db.faces.drop(),
  db.faces.insertOne({ data: { name: 'test' }, image: [] }),
  db.faces.deleteOne({ data: { name: 'test' } }),
];

printjson(res);
