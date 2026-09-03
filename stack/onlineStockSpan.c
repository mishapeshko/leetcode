#define MAX_N 10000

typedef struct {
    int start;
    int end;
    int* values;
    int* prevGreater;    
} StockSpanner;

StockSpanner* stockSpannerCreate() {
    StockSpanner* stSp = (StockSpanner*)malloc(sizeof(StockSpanner));
    stSp->start = 0;
    stSp->end = 0;
    stSp->values = (int*)malloc(sizeof(int)*MAX_N);
    stSp->prevGreater = (int*)malloc(sizeof(int)*MAX_N);
    return stSp;
}

int stockSpannerNext(StockSpanner* obj, int price) {
    obj->values[obj->end] = price;
    int j = obj->end-1;
    if(j == -1){
        obj->prevGreater[0] = -1;
        obj->end++;
        return 1;
    }
    while(j != -1 && obj->values[j] <= price){
        j = obj->prevGreater[j];
    }
    if(j == -1){
        obj->prevGreater[obj->end] = -1;
    }
    else{
        if(obj->values[j] > price){
            obj->prevGreater[obj->end] = j;
        }
        else{
            obj->prevGreater[obj->end] = -1;
        }
    }
    int item;
    if(obj->prevGreater[obj->end] == -1){
        item = obj->end+1;
    }
    else{
        item = obj->end-obj->prevGreater[obj->end];
    }
    obj->end++;
    return item;
}

void stockSpannerFree(StockSpanner* obj) {
    free(obj);
}
