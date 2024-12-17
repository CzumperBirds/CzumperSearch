package com.example.datasearchservice.api;

import com.example.datasearchservice.entity.Resource;
import com.example.datasearchservice.models.AdvancedSearchDTO;
import com.example.datasearchservice.service.SearchService;
import org.springframework.web.bind.annotation.*;

import java.util.Collections;
import java.util.List;

@RestController
@RequestMapping("/search")
public class SearchController {
    private final SearchService searchService;

    public SearchController(SearchService searchService) {
        this.searchService = searchService;
    }

//    @PostMapping("/")
//    public List<Resource> generalSearch(@RequestParam String searchPhrase) {
//        return searchService.generalSearch(searchPhrase);
//    }

    @PostMapping("/")
    public List<Resource> generalSearch(@RequestParam String searchPhrase) {
        AdvancedSearchDTO searchDTO = new AdvancedSearchDTO();
        searchDTO.content = searchPhrase;
        searchDTO.tags = List.of(searchPhrase.split(" "));
        return searchService.generalSearch(searchDTO.content, searchDTO.tags);
    }

    @PostMapping("/content")
    public List<Resource> searchByContent(@RequestParam String searchPhrase) {
        return searchService.searchByContent(searchPhrase);
    }

    @PostMapping("/tags")
    public List<Resource> searchByTags(@RequestBody List<String> searchTags) {
        return searchService.searchByTags(searchTags);
    }

}
