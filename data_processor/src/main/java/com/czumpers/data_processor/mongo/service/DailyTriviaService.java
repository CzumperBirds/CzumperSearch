package com.czumpers.data_processor.mongo.service;

import com.czumpers.data_processor.kafka.model.DailyTriviaConsumed;
import com.czumpers.data_processor.mongo.model.DailyTriviaDTO;
import com.czumpers.data_processor.mongo.repository.DailyTriviaRepository;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@AllArgsConstructor
public class DailyTriviaService {
    private final DailyTriviaRepository dailyTriviaRepository;

    public boolean isNewTrivia(DailyTriviaConsumed trivia) {
        return dailyTriviaRepository.findByDailyTriviaId(trivia.getId()).isEmpty();
    }

    public void saveTrivia(DailyTriviaConsumed trivia) {
        dailyTriviaRepository.save(new DailyTriviaDTO(trivia.getId()));
    }
}
