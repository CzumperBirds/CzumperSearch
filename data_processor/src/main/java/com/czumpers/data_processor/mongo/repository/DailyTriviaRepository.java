package com.czumpers.data_processor.mongo.repository;

import com.czumpers.data_processor.mongo.model.DailyTriviaDTO;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.Optional;

public interface DailyTriviaRepository extends MongoRepository<DailyTriviaDTO, String> {
    Optional<DailyTriviaDTO> findByDailyTriviaId(String dailyTriviaId);
}
