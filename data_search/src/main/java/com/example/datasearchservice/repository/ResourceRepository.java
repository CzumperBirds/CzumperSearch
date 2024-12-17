package com.example.datasearchservice.repository;

import com.example.datasearchservice.entity.Resource;
import org.springframework.cache.annotation.CacheConfig;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.data.elasticsearch.annotations.Query;
import org.springframework.data.elasticsearch.repository.ElasticsearchRepository;

import java.util.List;

@CacheConfig(cacheNames = "resources")
public interface ResourceRepository extends ElasticsearchRepository<Resource, String> {
    List<Resource> findByContentContaining(String content);

    @Query("{\"terms\": {\"tags\": ?0}}")
    List<Resource> findByTagsContaining(List<String> tags);


    @Query("""
            {
              "bool": {
                "should": [
                  {
                    "terms": {
                      "tags": #{#tags}
                    }   
                  },
                  {
                    "multi_match": {
                       "query": "#{#content}",
                       "fields": ["content", "source", "type"]
                    }
                  }
                ],
                "minimum_should_match": 1
              }
            }
            """)
    List<Resource> findByTagsOrContent(List<String> tags, String content);
}
