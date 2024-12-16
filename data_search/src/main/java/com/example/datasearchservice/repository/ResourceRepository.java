package com.example.datasearchservice.repository;

import com.example.datasearchservice.entity.Resource;
import org.springframework.cache.annotation.CacheConfig;
import org.springframework.data.elasticsearch.annotations.Query;
import org.springframework.data.elasticsearch.repository.ElasticsearchRepository;

import java.util.List;

@CacheConfig(cacheNames = "resources")
public interface ResourceRepository extends ElasticsearchRepository<Resource, String> {
    List<Resource> findByContentContaining(String content);

    @Query("{\"terms\": {\"tags\": ?0}}")
    List<Resource> findByTagsContaining(List<String> tags);

//    @Query("{\"bool\": {\"must\": [{\"terms\": {\"tags\": \"?0\"}}, {\"match\": {\"content\": \"?1\"}}]}}")
//    List<Resource> findByTagsAndContent(List<String> tags, String content);

    @Query("{\"bool\": {\"should\": ["
            + "{\"terms\": {\"tags\": ?0}},"
            + "{\"match\": {\"content\": ?1}}"
            + "], \"minimum_should_match\": 1}}")
    List<Resource> findByTagsOrContent(List<String> tags, String content);
}
//{ "query" : "?", "fields" : [ "name" ] }
//                        {"terms": {"tags": #{#tags}}},

//,
//        {"bool": {"must": [{"terms": {"tags": ?0}}]

//    @Query("""
//            {
//                "bool": {
//                    "should":[
//                        {"match": {"content": ?1}}
//                    ]
//                }
//            }""")

//        "      { \"match\": { \"content\": \"?1\" } }," +


//@Query("{" +
//        "  \"bool\": {" +
//        "    \"should\": [" +
//        "      { \"terms\": { \"query\" : \"?\", \"fields\" : [ \"tags\" ] } }" +
//        "    ]" +
//        "  }" +
//        "}")