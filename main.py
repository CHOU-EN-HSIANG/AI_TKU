from fastapi import FastAPI, HTTPException
from database import get_mysql_connection  # 從 database.py 引入連線函數

app = FastAPI()

@app.get("/home")
async def read_home():
    # 取得 MySQL 連接
    conn = get_mysql_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="無法連接 MySQL")
    
    cursor = conn.cursor()
    cursor.execute("SELECT 'Hello, MySQL!'")  # 示範查詢
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    
    return {"message": result[0]}

@app.get("/LRT")
async def read_lrt():
    return {"message": "這是 LRT 頁面"}

@app.get("/Bus")
async def read_bus():
    return {"message": "這是 Bus 頁面"}

@app.get("/YouBike")
async def read_youbike():
    return {"message": "這是 YouBike 頁面"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
