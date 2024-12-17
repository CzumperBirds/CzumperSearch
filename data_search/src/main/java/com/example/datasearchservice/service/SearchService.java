package com.example.datasearchservice.service;

import com.example.datasearchservice.entity.Resource;
import com.example.datasearchservice.models.AdvancedSearchDTO;
import com.example.datasearchservice.repository.ResourceRepository;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.stereotype.Service;


import java.util.List;

@Service
public class SearchService {
    private final ResourceRepository repository;

    public SearchService(ResourceRepository repository) {
        this.repository = repository;
    }
    public List<Resource> searchByContent(String content) {
        return repository.findByContentContaining(content);
    }
    public List<Resource> searchByTags(List<String> tags) {
        return repository.findByTagsContaining(tags);
    }
    @Cacheable(value = "searchCache", key = "#searchPhrase")
    public List<Resource> generalSearch(String searchPhrase) {
        AdvancedSearchDTO searchDTO = new AdvancedSearchDTO();
        searchPhrase = searchPhrase.toLowerCase();
        searchDTO.content = searchPhrase;
        searchDTO.tags = List.of(searchPhrase.split(" "));
        return repository.findByTagsOrContent(searchDTO.tags, searchDTO.content);
    }

}
