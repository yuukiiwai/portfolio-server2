```
response = self.client.get(url)
response.content.decode('utf-8') <-これでtypeがstrのjsonが見られる
```