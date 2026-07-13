# 阶段交接模板

```text
stage:
objective:
status:

confirmed_facts:
- fact_id + 结论 + 证据

decisions:
- 判断及理由

constraints:
- 下一阶段不可忽略的约束

conflicts_and_unknowns:
- 冲突、假设和未验证项

invalidated_artifacts:
- 因本阶段结论失效的产物

rubric_result:
- passed / failed / partial

next_stage:
next_action:
gate: auto / notify / approve
```

交接应足以支持下一阶段，但不重复完整过程。
