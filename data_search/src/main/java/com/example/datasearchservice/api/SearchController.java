package com.example.datasearchservice.api;

import com.example.datasearchservice.entity.Employee;
import com.example.datasearchservice.service.SearchService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/search")
public class SearchController {
    private final SearchService searchService;
    public SearchController(SearchService searchService) {
        this.searchService = searchService;
    }

    @GetMapping("/{searchPhrase}")
    public List<Employee> search(@PathVariable("searchPhrase") String searchPhrase) {
        return searchService.search(searchPhrase);
    }
}
