from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(
    title="FastAPI Demo",
    description="一个简单的 FastAPI 服务端示例",
    version="1.0.0",
)


class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)
    description: Optional[str] = None


class ItemResponse(Item):
    id: int


_items: dict[int, Item] = {}
_next_id = 1


@app.get("/")
async def root():
    return {"message": "FastAPI Demo 服务运行中", "docs": "/docs"}


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/items", response_model=list[ItemResponse])
async def list_items():
    return [ItemResponse(id=item_id, **item.model_dump()) for item_id, item in _items.items()]


@app.get("/items/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int):
    item = _items.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="商品不存在")
    return ItemResponse(id=item_id, **item.model_dump())


@app.post("/items", response_model=ItemResponse, status_code=201)
async def create_item(item: Item):
    global _next_id
    item_id = _next_id
    _next_id += 1
    _items[item_id] = item
    return ItemResponse(id=item_id, **item.model_dump())


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="商品不存在")
    del _items[item_id]
    return {"message": "删除成功", "id": item_id}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("fastapi_demo:app", host="0.0.0.0", port=8000, reload=True)
