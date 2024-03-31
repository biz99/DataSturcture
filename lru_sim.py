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
        cache_sim = CacheSimulator(cache_slots)
        for line in lines:
            page = line.split()[0]
            cache_sim.do_sim(page)
        
        cache_sim.print_stats()
