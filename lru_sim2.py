from list.circularLinkedList import CircularLinkedList

class CacheSimulator:
    def __init__(self, cache_slots):
        self.cache_slots = cache_slots
        self.cache = []  # Add cache attribute to track cache contents
        self.cache_hit = 0
        self.tot_cnt = 1
    
    def do_sim(self, page):
        self.tot_cnt += 1
        
        if page in self.cache:
            self.cache.remove(page)
            self.cache.append(page)
            self.cache_hit += 1
        else:
            if len(self.cache) >= self.cache_slots:
                self.cache.pop(0)
            self.cache.append(page)
            
    def print_stats(self):
        print("cache_slot = ", self.cache_slots, "cache_hit = ", self.cache_hit, "hit ratio = ", self.cache_hit / self.tot_cnt)

if __name__ == "__main__":
    data_file = open("/Users/wonseok/Desktop/soongsil/lru_sim/DataSturcture/linkbench.trc")
    lines = data_file.readlines()

    for cache_slots in range(100, 1001, 100):
        cache_sim = CircularLinkedList()
        cache_hit = 0
        tot_cnt = 0
        
        for line in lines:
            tot_cnt += 1
            if line in cache_sim:
                cache_sim.remove(line)
                cache_sim.append(line)
                cache_hit += 1
            else:
                if cache_sim.size() >= cache_slots:
                    cache_sim.pop(0)
                cache_sim.append(line)
        hit_ratio = cache_hit / tot_cnt if tot_cnt > 0 else 0 
        print("cache_slot = ", cache_slots, "cache_hit = ", cache_hit, "hit ratio = ", "hit ratio =", hit_ratio)
                
        