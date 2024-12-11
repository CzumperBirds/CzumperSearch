package com.czumpers.data_processor.kafka.consumer;

import com.czumpers.data_processor.kafka.mapper.DailyTriviaMapper;
import com.czumpers.data_processor.kafka.model.DailyTriviaConsumed;
import com.czumpers.data_processor.kafka.model.ResourceProduced;
import com.czumpers.data_processor.kafka.producer.ResourceProducer;
import com.czumpers.data_processor.mongo.service.DailyTriviaService;
import com.fasterxml.jackson.core.JsonProcessingException;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Slf4j
@Service
@RequiredArgsConstructor
public class DailyTriviaConsumer {

    private final DailyTriviaService dailyTriviaService;
    private final DailyTriviaMapper dailyTriviaMapper;
    private final ResourceProducer resourceProducer;

    @KafkaListener(
            topics = "daily-trivia",
            groupId = "spring-middleman",
            properties = {"spring.json.value.default.type=com.czumpers.data_processor.kafka.model.DailyTriviaConsumed"}
    )
    public void consume(DailyTriviaConsumed trivia) {
        if (dailyTriviaService.isNewTrivia(trivia)) {
            log.info("#### -> New trivia saved -> id: {}", trivia.getId());
            dailyTriviaService.saveTrivia(trivia);
            ResourceProduced resource = dailyTriviaMapper.mapToResource(trivia);
            resourceProducer.sendMessage(resource);
        } else {
            log.info("#### -> Duplicate trivia -> id: {}", trivia.getId());
        }
    }
}
